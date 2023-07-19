import requests
import parsel
import csv
import os

# 动作片-长空之王
with open('动作片1-长空之王.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
for page in range(21,30):
    url = f'https://movie.douban.com/subject/35209731/comments?start={page * 20}&limit=20&status=P&sort=new_score'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    # 把response.text文本数据转换成selector对象
    selector = parsel.Selector(response.text)
    # 获取所有comment-item标签
    comment_list = selector.css('.comment-item')
    # 遍历出每个comment-item标签内容
    for comment in comment_list:
        # 获取comment-info类属性下面的a标签中的文本数据
        name = comment.css('.comment-info a::text').get().strip()
        time = comment.css('.comment-time::text').get().strip()
        content = comment.css('.short::text').get().strip()
        point = comment.css('.comment-info span:nth-child(3)').get().strip()[20:22]
        vote_count = comment.css('.votes.vote-count::text').get().strip()
        # print(name, time, content, point, vote_count)
        with open('动作片1-长空之王.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])