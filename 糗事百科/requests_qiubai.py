import requests
from lxml import etree
import time

header = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}


# 请求页面
def fetch_url(url):
    response = requests.get(url=url, headers=header)
    html = etree.HTML(response.content)
    return get_page(html)


# 解析页面
def get_page(html):
    # 用户名
    usernames = html.xpath("//div[@class='author clearfix']//h2/text()")
    username_list = [str(username).replace('\n', '') for username in usernames]
    # 段子
    jokes = html.xpath("//div[@class='content']/span[1]/text()")
    str_jokes = ''.join(joke for joke in jokes)
    joke_list = str_jokes.split('\n\n\n')[1:]
    # 点赞
    votes = html.xpath("//span[@class='stats-vote']/i/text()")
    # 评论
    comments = html.xpath("//span[@class='stats-comments']//i/text()")

    # 保存段子
    for user, joke, vote, comment in zip(username_list, joke_list, votes, comments):
        context = '%s || 点赞%s || 评论%s\n%s' % (user, comment, vote, joke.replace('\n', '')) + '\n'
        print(context)
        save_jokes(context.encode('utf-8'))


def save_jokes(context):
    with open('qiubai.txt', 'ab') as f:
        f.write(context)
        f.flush()


if __name__ == '__main__':
    for i in range(1, 14):
        url = 'https://www.qiushibaike.com/hot/page/' + str(i)
        fetch_url(url)
        print('-----------------  第%s页  ---------------------' % i)
        time.sleep(2)
