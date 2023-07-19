import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import Birch
import warnings
warnings.filterwarnings("ignore")

# 读取文本数据
with open('test1.txt', 'r', encoding='utf-8') as f:
    documents = f.readlines()[:100]

# 读取停用词
stopword_path = "stop_words.txt"
with open(stopword_path, 'r', encoding='utf-8') as f:
    stop_words = [line.strip() for line in f]

# 分词处理
corpus = []
for doc in documents:
    words = jieba.cut(doc.strip())
    corpus.append(' '.join(words))
# print(corpus)

# 4.1 文本转换成词袋模型(词频作为统计指标)   加载停用词,添加词语进词袋时会过滤停用词
countVectorizer = CountVectorizer(stop_words=stop_words, analyzer="word")
count_v = countVectorizer.fit_transform(corpus)

# 4.2 词频统计指标转换 tf-idf统计指标  (不是必须的,用哪种指标根据具体业务来看)
tfidfTransformer = TfidfTransformer()
tfidf = tfidfTransformer.fit_transform(count_v)
# print(tfidf.toarray())

# birch聚类算法
'''
    tf-idf统计指标作为数据
    将参数设为None, 自动分类
'''
birch_cluster = Birch(n_clusters=None)
birch_result = birch_cluster.fit_predict(tfidf)
print("Predicting result: ", birch_result)
print(f'num_clusters: {max(birch_result)+1}')
# 自动划分为92类
