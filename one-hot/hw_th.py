import pandas as pd

df_th = pd.read_csv('thyroidDF甲状腺.csv', encoding='gbk')
# 数据类型
print(df_th.info())

# 独热编码
df_th1 = pd.get_dummies(df_th, columns=['是否服用甲状腺素', '是否生病', '患者是否接受过甲状腺手术', '是否正在接受 I131 治疗', '是否患有肿瘤', '是否在血液中测量了T3'])
print(df_th1)