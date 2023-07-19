import pandas as pd
import numpy as np
from gensim.models import Word2Vec
import jieba
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# 读取动作片评论数据集
data = pd.read_csv(r'./整理后数据/merged_action.csv')

# 加载Word2Vec模型
model = Word2Vec.load(r'./segmentation_wordcloud/word2vec模型/word2vec_action.model').wv

# 定义获取特征矩阵的函数
def getVector_v1(cutWords, word2vec_model):
    count = 0
    article_vector = np.zeros(word2vec_model.vector_size)
    for cutWord in cutWords:
        if cutWord in word2vec_model.key_to_index:
            article_vector += word2vec_model.get_vector(cutWord)
            count += 1
    if count != 0:
        return article_vector / count
    else:
        return np.zeros(word2vec_model.vector_size)



# 分词处理
list_all = []
data['评论内容'] = data['评论内容'].astype(str)
for sentence in data['评论内容']:
    words = list(jieba.cut(sentence))
    list_all.append(words)

# 生成特征矩阵
startTime = time.time()
vector_list = []
i = 0
for cutWords in list_all:
    i += 1
    if i % 1000 == 0:
        print('前%d 篇评论形成词向量花费%.2f 秒' % (i, time.time() - startTime))
    vector = getVector_v1(cutWords, model)
    vector_list.append(vector)
X = np.array(vector_list)
print('Total Time You Need To Get X: %.2f 秒' % (time.time() - startTime))
X.dump('sat_dissat_vector.txt')

# 标签编码
labelEncoder = LabelEncoder()
y = labelEncoder.fit_transform(data['情感'])

# 划分数据集
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0)



# 构建逻辑回归模型
logistic_model = LogisticRegression()
logistic_model.fit(train_X, train_y)
logistic_score = logistic_model.score(test_X, test_y)


# 输出分类报告
report = classification_report(test_y, logistic_model.predict(test_X), labels=[0, 1], target_names=['正向情感', '负向情感'],zero_division=1)
print(report)

# 计算AUC值
auc_score = roc_auc_score(test_y, logistic_model.predict_proba(test_X)[:, 1], multi_class='ovr')
print('AUC Score:', auc_score)

# 构建随机森林模型
rf = RandomForestClassifier(
    criterion='entropy',
    n_estimators=10000,
    min_samples_split=100,
    min_weight_fraction_leaf=0.05
)
rf.fit(train_X, train_y)
y_pred = rf.predict(test_X)
print('分类预测值：', y_pred)
