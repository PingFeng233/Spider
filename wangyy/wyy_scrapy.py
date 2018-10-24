import requests
from lxml import etree
import execjs
import json

HEADERS = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
}

COOKIES = {
    '_ntes_nnid': 'ec120dab4cb75d32efff994a79761982,1526465501219',
    '_ntes_nuid': 'ec120dab4cb75d32efff994a79761982',
    'WM_TID': 'FZLkww%2BCjeG4zs6k2JRBmorJ7LyK3ktq',
    '_iuqxldmzr_': '32',
    'usertrack=': 'ezq0pVsqGVWv6TU2BFkRAg==',
    '_ga': 'GA1.2.2011309267.1529485656',
    '__utmz': '94650624.1535794588.26.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__f_': '1536572085949',
    'vjuids': '51bf42042.165d5f2775c.0.2dd86b31833e8',
    'vjlast': '1536892762.1536892762.30',
    'vinfo_n_f_l_n3': 'd15e8dcff4df30ec.1.0.1536892762205.0.1536892772593',
    '__utma': '94650624.134579790.1527819164.1535794588.1537866440.27',
    '__utmc': '94650624',
    'JSESSIONID-WYYY': 'GNseqDz94UVvaXcD70NhuKMYy2gYf7%5CcRJoSzptRw%2FGjDuSCoIsICwCEVZQD%2Fvrx0WTSzJu8utkcGkfiZZeizvHBdOgog4%5CtlJgO2gRqXep5hhIDbF1AH%2FCDj7apCp2pJfjgVSn3kXNY64yHb0uv9ba5wvzmGYFz2e%2FXfucKQEl7%2F5ed%3A1537869978586',
    '__utmb': '94650624.24.10.1537866440',
    'WM_NI': 'oAaUCJKpN2KFBbJ%2FQW6BkPhOtqtc2DszhZ0v7CICUV%2FXqY31VQayVGucQ%2FPP3nR%2FDjPLPVJ%2BEzF8ZJD8WGG1QDcfjIzOGYLO%2FcBOBWx7xQtxpWRmQnEMxJHuHTjEivJjQVk%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eea2e47f83f0bba8f33bacb88bb2d14e939e9b84ee6e87bd8ea4db70bbeeb9d3c52af0fea7c3b92aad9fafb6c24289b082d3ca4e82be86d0d45df69ea5b1eb45b8afbc84b150b1a6a8bbb37ef59d87a4d85eed88bfbab23b968faf9ad54db7bd9fd0d35cf1b29ed0c7629494a0b7c92187a68ad9d94288e899a8c63b939cad87e943ba9189bacf45edbd8eb0c15dbce9b8b2f774b4899e8ed4668793b8abcb7f8c8ca6a6ec7e8ab69fb7ea37e2a3',
}


def parse_songs(url):
    r = requests.get(url, headers=HEADERS, cookies=COOKIES)
    html = etree.HTML(r.text)
    datas = html.xpath("//ul[@class='f-hide']/li/a")[:20]
    for data in datas:
        try:
            song_id = data.xpath("./@href")[0].split('=')[-1]
            song_name = data.xpath("./text()")[0]
            params, encSecKey = get_params_encSecKey(song_id)
            real_url = get_song(params, encSecKey)
            save_songs(real_url, song_name)
        except:
            pass


def get_params_encSecKey(song_id):
    d = '{"ids":"[%s]","br":128000,"csrf_token":""}' % song_id
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    js = open('wyy.js').read()
    res = execjs.compile(js).call('d', d, e, f, g)
    params = res.get('encText', None)
    encSecKey = res.get('encSecKey', None)
    return params, encSecKey


def save_songs(song_url, song_name):
    r = requests.get(song_url)
    with open('music/%s.mp3' % song_name, 'wb')as f:
        f.write(r.content)
    print('------%s  下载完成-------' % song_name)


def get_song(params, encSecKey):
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    data = {
        'params': params,
        'encSecKey': encSecKey
    }
    r = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    song_url = json.loads(r.text)['data'][0]['url']
    return song_url


if __name__ == '__main__':
    top_url = 'https://music.163.com/discover/toplist'
    parse_songs(top_url)