'''
# new:      20230921
# syz edit
# handin:   20230927
# 用Python编程对Flower.dat图像用如下拉普拉斯算子进行空间滤波和增强：np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# (图像边缘采用复制填充方式)
# 编写Python程序，输出并绘制结果。
# Flower数据：1024×1024, np.uint8
'''

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

Laplace = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# img = spectral.envi.open('Flower.hdr', 'Flower.dat')  # (1024, 1024, 1)

'''Data Source: '.\Flower.dat'
# # Rows:           1024
# # Samples:        1024
# # Bands:             1
# Interleave: BSQ
# Quantization: 8 bits
# Data format: uint8'''

# read from file
origin_data = np.fromfile('Flower.dat', dtype=np.uint8)
origin_data.shape = 1024, 1024

fig = plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(origin_data, cmap='gray')     # (x[:,:,[2,1,0]])
# plt.savefig('Flower_origin.png')
plt.title("Flower_origin.png")

# padding by copy
padding_data = np.insert(origin_data, 0, origin_data[0], axis=0)  # padding 0th row
padding_data = np.insert(padding_data, origin_data.shape[0], padding_data[origin_data.shape[0]],
                         axis=0)  # padding last row
padding_data = np.insert(padding_data, [0], padding_data[:, 0:1], axis=1)
padding_data = np.insert(padding_data, [origin_data.shape[0]],
                         padding_data[:, origin_data.shape[0]:origin_data.shape[0] + 1], axis=1)

# multiple with Laplace Operator
Laplace_data = np.zeros((1024, 1024), dtype=np.uint8)
for row in range(1, 1025):
    for col in range(1, 1025):
        origin_matrix = padding_data[row - 1:row + 2, col - 1:col + 2]
        Laplace_data[row - 1][col - 1] = abs(np.sum(Laplace * origin_matrix))

enhance_data = origin_data + Laplace_data
plt.subplot(2, 2, 2)
plt.imshow(Laplace_data, cmap='gray')
plt.title("Flower_Laplace.png")
plt.subplot(2, 2, 3)
plt.imshow(enhance_data, cmap='gray')
# plt.savefig('Flower_enhance.png')
plt.title("Flower_enhance.png")
fig.tight_layout(pad=1, w_pad=0, h_pad=3)
plt.show()

Flower_origin = Image.fromarray(origin_data)
Flower_origin.save("Flower_origin.png")
Flower_Laplace = Image.fromarray(Laplace_data)
Flower_Laplace.save("Flower_Laplace.png")
Flower_enhance = Image.fromarray(enhance_data)
Flower_enhance.save("Flower_enhance.png")
