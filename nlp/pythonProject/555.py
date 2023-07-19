import numpy as np
import pandas as pd

# 从CSV文件读取数据集
data = pd.read_csv(r'./整理后数据/merged_action.csv')

# 提取包含类别的列（假设类别列名为 'class'）
class_column = data['情感']

# 使用numpy.unique获取唯一类别
unique_classes = np.unique(class_column)

# 打印唯一类别
print(unique_classes)
