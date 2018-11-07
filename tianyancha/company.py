import requests
import json

companies = {}
with open('companies.txt', 'a',encoding='utf-8')as f:
    for i in range(20):
        url = "https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=100&cityId=765&" \
              "workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&" \
              "kt=3&lastUrlQuery=%7B%22jl%22:%22765%22%7D&rt=cc975bed189c4e74bf42bc2b2598f9a4&_v=0.11068914&" \
              "x-zp-page-request-id=35fe189bf071495ca40a8abfde61a72c-1541040183290-173141".format(str(i*100))
        r = requests.get(url)
        datas = json.loads(r.text)

        for data in datas['data']['results']:
            company = data['company']['name']
            if not companies.get(company, None):
                companies[company] = 1
                f.write(company + '\n')
                f.flush()
        print('-------第{}页------'.format(i+1))
