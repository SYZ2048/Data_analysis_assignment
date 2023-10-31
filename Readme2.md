# Readme2

### 运行

当前文件夹下应包括`Flower.dat`, `Flower.hdr`, `2_1.py`

##### 运行命令

```python
python 2_1.py
```

运行后，当前文件夹下产生`Flower_origin.png`, `Flower_Laplace.png`, `Flower_enhance.png`,

### 代码思路

##### 读取原始图像，结果如图

```python
# read from file
origin_data = np.fromfile('Flower.dat', dtype=np.uint8)
origin_data.shape = 1024, 1024

fig = plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(origin_data, cmap='gray')    
plt.title("Flower_origin.png")
```

##### 拉普拉斯过滤

首先对矩阵进行复制填充，以解决图像边界处的运算问题，依次复制第一行、最后一行、第一列、最后一列，得到填充矩阵

```python
padding_data = np.insert(origin_data, 0, origin_data[0], axis=0)  # padding 0th row
padding_data = np.insert(padding_data, origin_data.shape[0], padding_data[origin_data.shape[0]],
                         axis=0)  # padding last row
padding_data = np.insert(padding_data, [0], padding_data[:, 0:1], axis=1)
padding_data = np.insert(padding_data, [origin_data.shape[0]],
                         padding_data[:, origin_data.shape[0]:origin_data.shape[0] + 1], axis=1)
```

然后对填充矩阵中的所有3*3子矩阵与拉普拉斯算子进行矩阵乘法，得到的矩阵中的元素相加再取绝对值，赋值为子矩阵中心位置的像素值，得到锐化后的图像

```python
# multiple with Laplace Operator
Laplace_data = np.zeros((1024, 1024), dtype=np.uint8)
for row in range(1, 1025):
    for col in range(1, 1025):
        origin_matrix = padding_data[row - 1:row + 2, col - 1:col + 2]
        Laplace_data[row - 1][col - 1] = abs(np.sum(Laplace * origin_matrix))
```

将原始图像和锐化图像相加得到增强图像

```python
enhance_data = origin_data + Laplace_data
```

##### 输出结果并保存图像

```python
enhance_data = origin_data + Laplace_data
plt.subplot(2, 2, 2)
plt.imshow(Laplace_data, cmap='gray')
plt.title("Flower_Laplace.png")
plt.subplot(2, 2, 3)
plt.imshow(enhance_data, cmap='gray')
plt.title("Flower_enhance.png")
fig.tight_layout(pad=1, w_pad=0, h_pad=3)
plt.show()

Flower_origin = Image.fromarray(origin_data)
Flower_origin.save("Flower_origin.png")
Flower_Laplace = Image.fromarray(Laplace_data)
Flower_Laplace.save("Flower_Laplace.png")
Flower_enhance = Image.fromarray(enhance_data)
Flower_enhance.save("Flower_enhance.png")
```

### 实验结果

依次为原始图像、拉普拉斯滤波图像、增强图像

![image-20230925205033886](C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20230925205033886.png)

