import pandas as pd

# 读取数据
df = pd.read_excel('./all_data.xlsx')

# 获取列名
column_names = df.columns.tolist()

# 计算每个特征与合格率的关联性
correlations = df[column_names].corr()['合格率']

# 显示关联性结果
print(correlations)
