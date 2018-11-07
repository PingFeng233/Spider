import re
import random
import time
import requests
from lxml import etree
from settings import Cookies, Headers, Words_list, Proxy_Pool, User_Agent_Pool


def prase_html(url):
    proxies = random.choice(Proxy_Pool)
    Headers['User-Agent'] = random.choice(User_Agent_Pool)
    r = requests.get(url, cookies=Cookies, headers=Headers, proxies=proxies, verify=False)
    html = etree.HTML(r.text)
    print(r.text)
    datas = html.xpath("//div[@class='review-words']|//div[@class='review-words Hide']")
    with open('good.txt', 'a', encoding='gbk')as f:
        for data in datas:
            line = replace_span(data)
            comment = ''.join(etree.HTML(line).xpath("//div/text()")).strip() + '\n'
            print(comment)
            f.write(comment)
            f.flush()


def replace_span(data):
    css = open('words.css', 'r').read()
    # 获取html评论节点代码
    data = etree.tostring(data, encoding='utf-8').decode('utf-8')
    # 计算替换span标签
    spans = re.findall('<span class="(cv-.*?)"/>', data)
    for span in spans:
        res = re.findall(".%s{background: -(\d+)\.0px -(\d+)\.0px;}" % span, css)[0]
        x = int((int(res[1]) - 7) / 30)
        y = int(int(res[0]) / 14)
        word = Words_list[x][y]
        data = data.replace('<span class="%s"/>' % span, word)
    return data


if __name__ == '__main__':
    for i in range(100):
        url = "http://www.dianping.com/shop/2044996/review_all/p%s?queryType=reviewGrade&queryVal=good" % (str(i))
        prase_html(url)
        print('-------------第{}页--------------'.format(i + 1))
        time.sleep(random.random() * random.randint(2, 10))
