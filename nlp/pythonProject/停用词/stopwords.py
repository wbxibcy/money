import pandas as pd

# 读取语料库数据
data = pd.read_csv(r'C:\Users\90586\PycharmProjects\pythonProject\merged.csv')

# 统计词频
word_counts = {}
for content in data['content']:
    words = content.split()  # 假设语料库中的文本是以空格分隔的词语
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# 根据词频选择停用词
stopwords = []
for word, count in word_counts.items():
    # 自定义筛选条件，根据需求进行修改
    if count > 800:  # 假设频率超过1000为停用词
        stopwords.append(word)

# 将停用词保存到文件
with open('stopwords1.txt', 'w', encoding='utf-8') as f:
    for word in stopwords:
        f.write(word + '\n')