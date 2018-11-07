import requests
import json
import time
from urllib.request import urlopen
from PIL import Image, ImageEnhance
from aip import AipOcr
from settings import *


# 保存验证码图片
def get_verify_img():
    url = "http://antirobot.tianyancha.com/captcha/getCaptcha.json?t="
    r = requests.get(url)
    img_a_url = 'data:image/png;base64,' + json.loads(r.text)['data']['targetImage']
    img_b_url = 'data:image/png;base64,' + json.loads(r.text)['data']['bgImage']
    # 验证码id
    captchaId = json.loads(r.text)['data']['id']
    with open('a.png', 'wb')as f:
        r = urlopen(img_a_url)
        f.write(r.read())
    with open('b.png', 'wb')as f:
        r = urlopen(img_b_url)
        f.write(r.read())
    return captchaId


# 验证验证码
def checkCaptcha():
    captchaId = get_verify_img()
    clickLocs = parse_captcha()
    url = "https://antirobot.tianyancha.com/captcha/checkCaptcha.json?" \
          "captchaId={}&clickLocs={}".format(captchaId, clickLocs)
    r = requests.get(url)
    if r.status_code == 200:
        state = json.loads(r.text)['state']
        # {"state":"ok","message":"","special":"","data":null}
        if state == 'ok':
            # 验证成功
            return 1
    time.sleep(3)
    # 验证失败或者请求失败
    checkCaptcha()


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 解析验证码
def parse_captcha():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image_a = get_file_content('a.png')
    image_b = get_file_content('b.png')
    options = {}
    options["detect_direction"] = "true"
    # 高精度版会准确一点
    img_a_datas = client.basicAccurate(image_a, options)
    # img_b需要坐标信息
    img_b_datas = client.general(image_b)
    # 图片A中的文字
    a_words = [i['words'] for i in img_a_datas['words_result']]
    print(a_words)
    # 所有图片B的文字及坐标
    b_words = {}
    for word in img_b_datas['words_result']:
        key = word['words']
        value_x = word['location']['left']
        value_y = word['location']['top']
        b_words[key] = {'x': value_x, 'y': value_y}
    print(b_words)
    # 验证码的坐标
    clickLocs = []
    for i in a_words:
        for k, v in b_words.items():
            if i == k:
                clickLocs.append(v)
    print(clickLocs)
    return clickLocs


def enhance_img(imgPath):
    im = Image.open(imgPath)
    # 下面为增强部分
    enh_con = ImageEnhance.Contrast(im)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    # image_contrasted.show()

    # 增强亮度
    enh_bri = ImageEnhance.Brightness(image_contrasted)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    # image_brightened.show()
    # 增强对比度
    enh_col = ImageEnhance.Color(image_brightened)
    color = 1.5
    image_colored = enh_col.enhance(color)
    # image_colored.show()
    # 增强锐度
    enh_sha = ImageEnhance.Sharpness(image_colored)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    # image_sharped.show()

    # 灰度处理部分
    im2 = image_sharped.convert("L")
    return im2


if __name__ == '__main__':
    checkCaptcha()
