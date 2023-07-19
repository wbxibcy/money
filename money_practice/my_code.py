import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 打开文件
df = pd.read_excel('互联网金融练习数据.xlsx')
print(df)

print(df.info())

# 处理空值
# 假设空值用NaN表示
# df = df.fillna(0)  # 将空值填充为0
df = df.fillna(method='backfill', axis=0, inplace=False) # 用后面一个值填充

# 根据是否逾期进行数据分组
groups = df.groupby('是否逾期')

# 遍历分组并输出统计信息
for name, group in groups:
    print('逾期状态:', name)
    print(group.describe())  # 输出统计信息，如均值、标准差等

# 查看元素个数并且转换
print(df['是否逾期'].value_counts())
df['是否逾期'] = df['是否逾期'].map( {'未逾期': 1, '逾期': 0} ).astype(int)

# 获取列名
column_names = df.columns.tolist()

# 计算每个特征与是否逾期的关联性
correlations = df[column_names].corr()['是否逾期']

# 显示大于0.25的关联性结果
print(correlations[(abs(correlations) > 0.25) & (abs(correlations) != 1)])

# 新特征的列名
new_colums = correlations[(abs(correlations) > 0.25) & (abs(correlations) != 1)].index.values.tolist()      
print(new_colums)
