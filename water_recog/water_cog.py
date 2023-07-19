import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageFont
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from data_procss import get_img_data, var
from tools import save_model, load_model

classes = {0: "清澈", 1: "浅绿色", 2: "灰蓝色", 3: "黄褐色", 4: "茶褐色"}


def train(save_model_path="model.pk"): 
    data, labels = get_img_data("water_images/")  # 数据预处理
    data_train, data_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.2)  # 将专家样本拆分为训练集和测试集
    Dtc = DecisionTreeClassifier().fit(data_train, labels_train)  # 模型训练
    pre = Dtc.predict(data_test)  # 模型预测
    save_model(Dtc, save_model_path=save_model_path)
    accuracy = sum(pre == labels_test) / len(pre)  # 预测精度
    c = confusion_matrix(labels_test, pre)  # 混淆矩阵
    report = classification_report(labels_test, pre)  # 分类性能报告
    print("准确率")
    print(accuracy)
    print("混淆矩阵")
    print(c)
    print("分类性能报告")
    print(report)


def detect(img_path, model_path="model.pk"):
    dtc_model = load_model(model_path)
    img = Image.open(img_path)  # 读取图片数据
    M, N = img.size  # 像素矩阵的行列数
    box = (M / 2 - 50, N / 2 - 50, M / 2 + 50, N / 2 + 50)
    region = img.crop(box)  # 用crop方法截取图像的中心区域
    img_tran = np.zeros([9])
    # 数据预处理
    r, g, b = region.split()  # 分割像素通道
    rd = np.asarray(r)  # 把图片数据转换为数组
    gd = np.asarray(g)
    bd = np.asarray(b)

    # 求rgb均值
    img_tran[0] = rd.mean()  # 一阶颜色距
    img_tran[1] = gd.mean()
    img_tran[2] = bd.mean()

    # 求rgb标准差
    img_tran[3] = rd.std()  # 二阶颜色距
    img_tran[4] = gd.std()
    img_tran[5] = bd.std()

    # 求var
    img_tran[6] = var(rd)  # 三阶颜色距
    img_tran[7] = var(gd)
    img_tran[8] = var(bd)

    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式 这里的SimHei.ttf需要有这个字体
    pre = dtc_model.predict(np.array([img_tran]))
    fontStyle = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
    if int(pre[0]) > 2:  # 通过该值去判断的异常不异常，大于1就为异常，小于1为正常
        print("该水质出现异常")
        text = "水质检测结果是：异常，" + classes[int(pre[0])]
    else:
        text = "水质检测结果是：正常，" + classes[int(pre[0])]
        print("该水质正常")

    # 绘制文本
    fontStyle = ImageFont.truetype("simhei.ttf", 20)
    draw.text((20, 20), text, (200, 0, 0), font=fontStyle)
    img.show()
    save_result_path = "result.jpg"
    img.save(save_result_path)
    print("检测图片保存路径" + save_result_path)
    print("预测结果是：" + classes[int(pre[0])])

load_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy']) 
history = model.fit(X_train, Y_train, epochs=200, batch_size=10, verbose=2, validation_split=0.33)
acc = history.history['accuracy'] 
val_acc = history.history['val_accuracy'] 
loss = history.history['loss'] 
val_loss = history.history['val_loss'] 
epochs = range(len(acc))
plt.plot(epochs,acc, 'b', label='Training accuracy') 
plt.plot(epochs, val_acc, 'r', label='validation accuracy') 
plt.title('Training and validation accuracy') 
plt.legend(loc='lower right') 
plt.figure()
plt.plot(epochs, loss, 'r', label='Training loss') 
plt.plot(epochs, val_loss, 'b', label='validation loss') 
plt.title('Training and validation loss') 
plt.legend() 
plt.show()


train() # 水色图像训练，训练好的模型保存在 model.pk
detect(img_path="water_images/2_3.jpg") # 可以更改图片路径进行检测