# import numpy as np
# import pandas as pd
# import torch
# import os
# import torch.nn as nn
# import torchvision.models as models
# import torchvision.transforms as transforms
# from PIL import Image
# # "ConcatDataset" and "Subset" are possibly useful when doing semi-supervised learning.
# from torch.utils.data import ConcatDataset, DataLoader, Subset, Dataset
# from torchvision.datasets import DatasetFolder, VisionDataset
# # This is for the progress bar.
# from tqdm.auto import tqdm
# import random    


# myseed = 6666  # set a random seed for reproducibility
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# np.random.seed(myseed)
# torch.manual_seed(myseed)
# if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(myseed)

# # Normally, We don't need augmentations in testing and validation.
# # All we need here is to resize the PIL image and transform it into Tensor.
# test_tfm = transforms.Compose([
#     transforms.Resize((128, 128)),
#     transforms.ToTensor(),
# ])

# test_tfm_augment = transforms.Compose([
#     # Resize the image into a fixed shape (height = width = 128)
#     transforms.Resize((128, 128)),
#     transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1), # 随机改变图像的亮度、对比度、饱和度和色调
#     transforms.RandomRotation(degrees=(0, 30)),
#     transforms.RandomAdjustSharpness(sharpness_factor=2, p=0.5), # 随机锐度
#     transforms.RandomAutocontrast(p=0.5), # 随机对比度
#     transforms.RandomHorizontalFlip(p=0.5), # 随机水平翻转    

# ])


# # However, it is also possible to use augmentation in the testing phase.
# # You may use train_tfm to produce a variety of images and then test using ensemble methods

# train_tfm = transforms.Compose([
#     # Resize the image into a fixed shape (height = width = 128)
#     transforms.Resize((128, 128)),
#     # You may add some transforms here.
#     # syzedit:

#     transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1), # 随机改变图像的亮度、对比度、饱和度和色调
#     # transforms.GaussianBlur(kernel_size=5, sigma=(0.1, 2.0)),
#     # transforms.RandomPerspective(distortion_scale=0.5, p=0.5), # 随机改变透视
#     transforms.RandomRotation(degrees=(0, 30)),
#     # transforms.ElasticTransform(alpha=50.0), # 随机局部扭曲 alpha 变形的程度
#     transforms.RandomAdjustSharpness(sharpness_factor=2, p=0.5), # 随机锐度
#     transforms.RandomAutocontrast(p=0.5), # 随机对比度
#     transforms.RandomHorizontalFlip(p=0.5), # 随机水平翻转
#     # transforms.RandomVerticalFlip(p=0.5), # 随机垂直翻转

#     # ToTensor() should be the last one of the transforms.
#     transforms.ToTensor(),
# ])


# # "cuda" only when GPUs are available.
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # The number of batch size.
# batch_size = 64

# # The number of training epochs.
# n_epochs = 8

# # If no improvement in 'patience' epochs, early stop.
# patience = 300

# # For the classification task, we use cross-entropy as the measurement of performance.
# criterion = nn.CrossEntropyLoss()

# class FoodDataset(Dataset):

#     def __init__(self,path,tfm=test_tfm,files = None):
#         super(FoodDataset).__init__()
#         self.path = path
#         self.files = sorted([os.path.join(path,x) for x in os.listdir(path) if x.endswith(".jpg")])
#         if files != None:
#             self.files = files

#         self.transform = tfm

#     def __len__(self):
#         return len(self.files)

#     def __getitem__(self,idx):
#         fname = self.files[idx]
#         im = Image.open(fname)
#         im = self.transform(im)

#         try:
#             label = int(fname.split("/")[-1].split("_")[0])
#         except:
#             label = -1 # test has no label

#         return im,label

# test_set = FoodDataset("/kaggle/input/ml2023spring-hw3/test", tfm=test_tfm)
# test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=0, pin_memory=True)

# model = models.resnet50(weights=False) 
# # 更改全连接层以匹配目标类别的数量
# num_features = model.fc.in_features  # 获取全连接层(fc)的输入特征数
# num_classes = 11  # 11 classes
# model.fc = nn.Linear(num_features, num_classes)  # 替换最后的全连接层


# model_best = Classifier().to(device)
# model = ResNet50WithDropout(num_classes=11, dropout_rate=0.5)
model_best = model.to(device)
# model_best.load_state_dict(torch.load(f"{_exp_name}_best.ckpt"))

# test with ckpt file
model_best.load_state_dict(torch.load("/kaggle/input/testckpt/sample_best.ckpt"))

model_best.eval()
prediction = []

# with torch.no_grad():
#     for data,_ in tqdm(test_loader):
#         test_pred = model_best(data.to(device))
#         test_label = np.argmax(test_pred.cpu().data.numpy(), axis=1)
#         prediction += test_label.squeeze().tolist()

# syzedit: Test Time Augmentation
tta_steps = 5
weights = [0.2 / tta_steps] * tta_steps + [0.8]  # train_tfm + test_tfm权重

with torch.no_grad():
    for data, _ in tqdm(test_loader):
        tta_preds = []

        # 采用train_tfm对数据进行增强并预测
        for i in range(tta_steps):
            augmented_data = test_tfm_augment(data)
            test_pred = model_best(data.to(device))
            tta_preds.append(test_pred * weights[i])

        # 采用test_tfm进行预测
        test_pred = model_best(data.to(device))
        tta_preds.append(test_pred * weights[-1])

        # 加权平均TTA预测结果
        tta_preds = torch.sum(torch.stack(tta_preds), dim=0)

        # 得到最终预测标签
        test_label = torch.argmax(tta_preds, dim=1)
        prediction.extend(test_label.tolist())


# create test csv
# num to 4-digit string
def pad4(i):
    return "0" * (4 - len(str(i))) + str(i)


df = pd.DataFrame()
df["Id"] = [pad4(i) for i in range(len(test_set))]
df["Category"] = prediction
df.to_csv("submission.csv", index=False)
# df.to_csv("/kaggle/working/submission.csv",index = False)