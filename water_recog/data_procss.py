import os, re  # 调用os，re正则表达式
from PIL import Image  # 通过PIL库导入照片类
import numpy as np

# 自定义函数获取指定路径中的所有图片名称
path = 'water_images/'


def get_img_names(path=path):
    file_names = os.listdir(path)
    img_names = []
    for i in file_names:
        if re.findall('\d_\d+\.jpg$', i) != []:  # \d表示数字，\d+表示至少一个数字，\.运用\表示转意符号,$表示结尾
            img_names.append(i)  # append对元素i的追加
    return img_names


def var(rd):  # 求颜色通道的三阶颜色距
    mid = np.mean((rd - rd.mean()) ** 3)
    return np.sign(mid) * abs(mid) ** (1 / 3)


# 获取样本数据：计算均值、标准差、方差、作为样本数据，自变量data和标签 labels
def get_img_data(path=path):
    img_names = get_img_names(path=path)  # 获取所有图片的名称
    n = len(img_names)
    data = np.zeros([n, 9])  # data保存所有样本自变量
    labels = np.zeros([n])  # 样本标签
    for i in range(n):
        img = Image.open(path + img_names[i])  # 读取图片数据
        M, N = img.size  # 像素矩阵的行列数
        box = (M / 2 - 50, N / 2 - 50, M / 2 + 50, N / 2 + 50)
        region = img.crop(box)  # 用crop方法截取图像的中心区域
        region.show()
        # img.show()  #展示图片

        # 数据预处理
        r, g, b = region.split()  # 分割像素通道
        rd = np.asarray(r)  # 把图片数据转换为数组
        gd = np.asarray(g)
        bd = np.asarray(b)

        # 这里就是你那个图片中说的，求图像的颜色值，
        # 下面三行是求图像rgb的均值，
        data[i, 0] = rd.mean()  # 一阶颜色距
        data[i, 1] = gd.mean()
        data[i, 2] = bd.mean()

        # 下面三行是求图像rgb的标准差
        data[i, 3] = rd.std()  # 二阶颜色距
        data[i, 4] = gd.std()
        data[i, 5] = bd.std()
        # 下面三行是求图像rgb的方差
        data[i, 6] = var(rd)  # 三阶颜色距
        data[i, 7] = var(gd)
        data[i, 8] = var(bd)

        labels[i] = img_names[i][0]
    return data, labels
