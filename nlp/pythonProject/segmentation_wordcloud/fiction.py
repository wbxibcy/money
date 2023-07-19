import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gensim.models import Word2Vec

# 科幻片
data = pd.read_csv(r'C:\Users\90586\PycharmProjects\pythonProject\整理后数据\merged_fiction.csv')
df = data.copy()

data_stop = pd.read_csv(r'C:\Users\90586\PycharmProjects\pythonProject\停用词\stopwords.csv', encoding='gbk')
list_stop = [i for i in data_stop.iloc[:,0]]

list_content = df.iloc[:,2].astype(str)

list_words = []
set_words = set()

## list_generator:对每条评论分词
list_generator = map(jieba.cut,list_content)

## 把每条评论的分词加入放到list_words表中
for i in list_generator:
    for word in i:
        if word not in list_stop:
            list_words.append(word)
set_words = set(list_words)

dict_words = dict()
for key in set_words:
    dict_words[key] = list_words.count(key)

key = dict_words.keys()
value = dict_words.values()
data_count_frame = pd.DataFrame({'分词':key,'计数':value})

data_count_frame.to_csv('科幻片评论分词统计数据.csv',encoding='gbk')

# 语料准备
list_all = [list(jieba.cut(sentence)) for sentence in list_words]

# 将分词结果输入 word2vec 模型进行训练
model = Word2Vec(list_all, sg=0, vector_size=20, window=5, alpha=0.001, min_count=5, hs=0, negative=10, epochs=10, cbow_mean=1)

# 保存模型
model.save('word2vec_fiction.model')

# 生成词云图
text = " ".join(list_words)
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path="C:\\Users\\90586\\PycharmProjects\\pythonProject\\segmentation_wordcloud\\字体\\NotoSansSC-Regular.otf").generate(text)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()