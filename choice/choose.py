# https://allenwind.github.io/blog/10395/

import numpy as np
from scipy.stats import norm

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 原始数据

# 估计均值和标准差
mean, std_dev = norm.fit(data)

# 计算数据的概率密度函数值
pdf_values = norm.pdf(data, mean, std_dev)

# 归一化概率值
normalized_probs = pdf_values / np.sum(pdf_values)

# 选择符合正态分布的数据
size = 5  # 选择的数据个数
selected_data = np.random.choice(data, size=size, replace=False, p=normalized_probs)

print(selected_data)
