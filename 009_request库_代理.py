#encoding:utf-8

import requests

proxy = {
    '116.209.62.142':'9999'
}

url = 'http://www.httpbin.org/ip'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400',
           'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
           }

reponse = requests.get(url,headers=headers,proxies=proxy)

result = reponse.content.decode('utf-8') #解码
print(result)

print(reponse.url)
print(reponse.encoding)
print(reponse.status_code)





