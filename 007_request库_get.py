#encoding:utf-8

import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'}
reponse = requests.get('https://www.baidu.com/s',params={'wd':'杨幂'},headers=headers)
#print(reponse.text) #自动解码
result = reponse.content.decode('utf-8') #解码
print(result)

with open('request_get_lagou.html','w',encoding='utf-8') as fp:
    fp.write(reponse.content.decode('utf-8'))

print(reponse.url)
print(reponse.encoding)
print(reponse.status_code)





