import requests
import random
import time
from lxml import etree
from settings import *
from captcha import checkCaptcha


def start_parse():
    with open("companies.txt", 'r', encoding='utf-8') as f:
        while True:
            if not f.readline():
                break
            company = f.readline().replace("\n", "")
            url = "https://www.tianyancha.com/search?key=" + company
            Headers['User-Agent'] = random.choice(User_Agent_Pool)
            proxies = random.choice(Proxy_Pool)
            try:
                parse_company(url, proxies, Headers)
            except Exception as e:
                print('Error:{}'.format(e))


def parse_company(url, proxies, Headers):
    r = requests.get(url, headers=Headers, cookies=Cookies, proxies=proxies, verify=False)
    html = etree.HTML(r.text)
    title = html.xpath("//title/text()")[0]
    if title == "天眼查校验":
        checkCaptcha()
    datas = html.xpath('//div[@class="search-item"]')
    with open("company_info.txt", 'a', encoding='utf-8')as f:
        for data in datas:
            company_name = ''.join(data.xpath('.//div[@class="header"]/a//text()'))
            company_leader = ''.join(data.xpath('.//div[@class="info"]/div[1]/a/text()'))
            registe_money = ''.join(data.xpath('.//div[@class="info"]/div[2]/span/text()'))
            registe_date = ''.join(data.xpath('.//div[@class="info"]/div[3]/span/text()'))
            tel = ' | '.join(data.xpath('.//div[@class="contact"]/div[1]/span[2]/text()'))
            email = ''.join(data.xpath('.//div[@class="contact"]/div[2]/span[2]/text()'))
            score = data.xpath('.//div[@class="score"]/span[1]/text()')[0]
            line = company_name + '\t' + score + '\n' + '法人代表:' + company_leader + '\t' + '注册资本:' \
                   + registe_money + '\t' + '注册时间:' + registe_date + '\n' + '联系方式:' \
                   + tel + '\t' + '邮箱:' + email + '\n'
            print(line)
            f.write(line)
            f.flush()
    time.sleep(random.random() * random.randint(3, 10))


if __name__ == '__main__':
    start_parse()
