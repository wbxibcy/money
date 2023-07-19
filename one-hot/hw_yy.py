import pandas as pd

df_yy = pd.read_csv('大学生患抑郁症数据信息.csv', encoding='gbk')
# 数据类型
print(df_yy.info())

# 独热编码
df_yy1 = pd.get_dummies(df_yy, columns=['是否有抑郁症', '治疗药物'])
print(df_yy1)