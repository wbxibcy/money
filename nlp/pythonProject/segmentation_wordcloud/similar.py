# 导入训练好的Word2Vec模型
from gensim.models import Word2Vec

# 加载训练好的动作片模型
model = Word2Vec.load(r'C:\Users\90586\PycharmProjects\pythonProject\segmentation_wordcloud\word2vec模型\word2vec_action.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
# 输出相似单词及其相似度得分
print("动作片")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)


# 加载训练好的喜剧片模型
model = Word2Vec.load('C:\\Users\\90586\\PycharmProjects\\pythonProject\\segmentation_wordcloud\\word2vec模型\\word2vec_comedy.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
print("喜剧片")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)

# 加载训练好的科幻片模型
model = Word2Vec.load(r'C:\Users\90586\PycharmProjects\pythonProject\segmentation_wordcloud\word2vec模型\word2vec_fiction.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
print("科幻片")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)

# 加载训练好的爱情片模型
model = Word2Vec.load(r'C:\Users\90586\PycharmProjects\pythonProject\segmentation_wordcloud\word2vec模型\word2vec_love.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
print("爱情片")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)

# 加载训练好的悬疑片模型
model = Word2Vec.load(r'C:\Users\90586\PycharmProjects\pythonProject\segmentation_wordcloud\word2vec模型\word2vec_suspense.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
print("悬疑片")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)

# 加载训练好的五类电影总和模型
model = Word2Vec.load(r'C:\Users\90586\PycharmProjects\pythonProject\segmentation_wordcloud\word2vec模型\word2vec_all.model')
# 获取与指定单词最相似的单词
similar_words1 = model.wv.most_similar('故事', topn=5)
similar_words2 = model.wv.most_similar('表演', topn=5)
similar_words3 = model.wv.most_similar('情绪', topn=5)
similar_words4 = model.wv.most_similar('内容', topn=5)
similar_words5 = model.wv.most_similar('感受', topn=5)
print("五类电影总和")
print("与”故事“最相近的五个词及其相似度")
for word, similarity in similar_words1:
    print(word, similarity)
print("与”表演“最相近的五个词及其相似度")
for word, similarity in similar_words2:
    print(word, similarity)
print("与”情绪“最相近的五个词及其相似度")
for word, similarity in similar_words3:
    print(word, similarity)
print("与”内容“最相近的五个词及其相似度")
for word, similarity in similar_words4:
    print(word, similarity)
print("与”感受“最相近的五个词及其相似度")
for word, similarity in similar_words5:
    print(word, similarity)