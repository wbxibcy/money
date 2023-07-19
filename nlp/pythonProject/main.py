import requests
import parsel
import csv
import os

# 动作片-长空之王
with open('动作片-长空之王.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
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
        with open('动作片-长空之王.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-狙击之王：暗杀
with open('动作片-狙击之王：暗杀.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35904114/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('动作片-狙击之王：暗杀.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-暴风
with open('动作片-暴风.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35391267/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('动作片-暴风.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-奇门遁甲2
with open('动作片-奇门遁甲2.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35617081/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('动作片-奇门遁甲2.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-断网
with open('动作片-断网.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35043401/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('动作片-断网.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-目中无人
with open('动作片-目中无人.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35295405/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('动作片-目中无人.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 动作片-风再起时
with open('动作片-风再起时.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/26995475/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('动作片-风再起时.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])

# 喜剧片-人生路不熟
with open('喜剧片-人生路不熟.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35653205/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('喜剧片-人生路不熟.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-龙马精神
with open('喜剧片-龙马精神.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35595615/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('喜剧片-龙马精神.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-满江红
with open('喜剧片-满江红.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35766491/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('喜剧片-满江红.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-了不起的夜晚
with open('喜剧片-了不起的夜晚.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35814176/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('喜剧片-了不起的夜晚.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-保你平安
with open('喜剧片-保你平安.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35457272/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('喜剧片-保你平安.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-这个杀手不太冷静
with open('喜剧片-这个杀手不太冷静.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35505100/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('喜剧片-这个杀手不太冷静.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 喜剧片-带你去见我妈
with open('喜剧片-带你去见我妈.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35683855/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('喜剧片-带你去见我妈.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])

# 科幻片-流浪地球2
with open('科幻片-流浪地球2.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35591164/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('科幻片-流浪地球2.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-深海
with open('科幻片-深海.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/26649682/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('科幻片-深海.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-熊出没·伴我“熊芯”
with open('科幻片-熊出没·伴我“熊芯”.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/36123159/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('科幻片-熊出没·伴我“熊芯”.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-交换人生
with open('科幻片-交换人生.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['用户名', '评论时间', '评论内容', '评分', '赞同数'])
for page in range(0, 21):
        url = f'https://movie.douban.com/subject/35513968/comments?start={page * 20}&limit=20&status=P&sort=new_score'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
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
            with open('科幻片-交换人生.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-独行月球
with open('科幻片-独行月球.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35183042/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('科幻片-独行月球.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-冲出地球
with open('科幻片-冲出地球.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/27599400/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('科幻片-冲出地球.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 科幻片-明日战记
with open('科幻片-明日战记.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/26353671/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('科幻片-明日战记.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])

# 爱情片-这么多年
with open('爱情片-这么多年.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35591164/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片-这么多年.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-长沙夜生活
with open('爱情片-长沙夜生活.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35451891/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片-长沙夜生活.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-倒数说爱你
with open('爱情片-倒数说爱你.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35876337/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片-倒数说爱你.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-爱很美味
with open('爱情片-爱很美味.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35711450/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片-爱很美味.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-我们的样子像极了爱情
with open('爱情片-我们的样子像极了爱情.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/34913599/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片-我们的样子像极了爱情.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-我是真的讨厌异地恋
with open('爱情片-我是真的讨厌异地恋.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35057107/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('爱情片1-我是真的讨厌异地恋.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 爱情片-好想去你的世界爱你
with open('爱情片-好想去你的世界爱你.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35352389/comments?start={page * 20}&limit=20&status=P&sort=new_score'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
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
        with open('爱情片1-好想去你的世界爱你.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])

# 悬疑片-回廊亭
with open('悬疑片-回廊亭.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35401290/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-回廊亭.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-无名
with open('悬疑片-无名.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35372742/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-无名.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-检察风云
with open('悬疑片-检察风云.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/34434003/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-检察风云.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-纸人回魂
with open('悬疑片-纸人回魂.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/36200703/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-纸人回魂.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-神探大战
with open('悬疑片-神探大战.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/26995893/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-神探大战.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-山村狐妻
with open('悬疑片-山村狐妻.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35914264/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-山村狐妻.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])
# 悬疑片-远山淡影
with open('悬疑片-远山淡影.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名','评论时间','评论内容','评分','赞同数'])
for page in range(0,21):
    url = f'https://movie.douban.com/subject/35182979/comments?start={page * 20}&limit=20&status=P&sort=new_score'
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
        with open('悬疑片-远山淡影.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, time, content, point, vote_count])

# 动作-合并csv文件
def merge_action_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('动作'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged_action.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_action_filrs()
# 喜剧-合并csv文件
def merge_comedy_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('喜剧'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged_comedy.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_comedy_filrs()
# 科幻-合并csv文件
def merge_fiction_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('科幻'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged_fiction.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_fiction_filrs()
# 爱情-合并csv文件
def merge_love_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('爱情'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged_love.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_love_filrs()
# 悬疑-合并csv文件
def merge_suspense_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('悬疑'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged_suspense.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_suspense_filrs()

# 总-合并csv文件
def merge_filrs():
    files = os.listdir('.')
    for file in files:
        if file.lower().startswith('merged'):
            with open(file,'r', encoding='utf-8') as f:
                with open('merged.csv','a', encoding='utf-8') as f2:
                    f2.write(f.read())
merge_filrs()