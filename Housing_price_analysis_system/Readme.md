# Readme

# 二手房房价分析与预测系统

### 环境配置

##### 函数运行

##### 库支持

PyQt5



### 主界面

整个界面设计在Qt designer中实现

##### 背景图片

使用`QLabel`部件来插入图片，设置对应的图像为`background.png`，设置scaledContents来保证图像和Qlabel部件同步缩放

<img src="C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20231101183710736.png" alt="image-20231101183710736" style="zoom: 50%;" />

##### 五个功能按键

为了使图标显示在文本的上方，你需要修改工具栏的属性

1. 在`Property Editor`中，找到`toolButtonStyle`属性。
2. 将`toolButtonStyle`设置为`ToolButtonTextUnderIcon`

包括`各区二手房均价分析`, `各区二手房数量所占比例`, `全市二手房装修程度分析`, `热门户型均价分析`, `二手房售价预测`



### 功能处理

##### 各区二手房均价分析

二手房均价的条形图

##### 各区二手房数量所占比例

区域二手房数据及占比分析饼状图

##### 全市二手房装修程度分析

装修程度的条形图

##### 热门户型均价分析

热门户型均价的条形图

##### 二手房售价预测

二手房售价预测折线图

