# 导入训练好的Word2Vec模型
from gensim.models import Word2Vec

# 加载训练好的动作片模型
model = Word2Vec.load(r'./segmentation_wordcloud/word2vec模型/word2vec_all.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('心情', topn=5)
similar_words2 = model.wv.most_similar('感受', topn=5)

# 输出相似单词及其相似度得分
print("动作片")
print("与”心情“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
