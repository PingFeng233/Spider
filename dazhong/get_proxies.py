import requests
from lxml import etree
import os

Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.xicidaili.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


def save_html(url):
    r = requests.get(url)
    print(r.text)
    with open('xici.html', 'wb')as f:
        f.write(r.content)


def save_proxies():
    html = open('xici.html', encoding='utf-8').read()
    html = etree.HTML(html)
    datas = html.xpath("//table[@id='ip_list']/tr[position()>1]")
    with open('proxies.txt', 'a+')as f:
        for data in datas:
            ip = data.xpath("td[2]/text()")[0]
            port = data.xpath("td[3]/text()")[0]
            type = data.xpath("td[6]/text()")[0]
            f.write(type + '\t' + ip + '\t' + port + '\n')


def get_yun_proxies():
    html = open('xici.html', encoding='gbk').read()
    html = etree.HTML(html)
    datas = html.xpath("//tbody/tr")
    with open('proxies.txt', 'a+')as f:
        for data in datas:
            ip = data.xpath("td[1]/text()")[0]
            port = data.xpath("td[2]/text()")[0]
            type = data.xpath("td[4]/text()")[0]
            f.write(type + '\t' + ip + '\t' + port + '\n')


def test_proxy():
    test_url = "https://ip.cn"
    proxy_ok = []
    with open('proxies.txt', 'r')as f:
        while True:
            line_data = f.readline()
            if not line_data:
                break
            line = line_data.split('\t')
            proxies = {line[0].lower(): "http://{}:{}".format(line[1], line[2].replace('\n', '')).lower()}
            print(proxies)
            try:
                r = requests.get(test_url, proxies=proxies, timeout=10, verify=False)
                print(r.status_code)
                if r.status_code == 200:
                    with open('https.txt', 'a')as g:
                        g.write(line_data)
                        g.flush()
                    proxy_ok.append(proxies)
            except:
                pass
        print('=========')
        print(proxy_ok)


if __name__ == '__main__':
    for i in range(1, 8):
        url = "http://www.ip3366.net/free/?stype=1&page=" + str(i)
        save_html(url)
        get_yun_proxies()
        test_proxy()
        os.remove('proxies.txt')
