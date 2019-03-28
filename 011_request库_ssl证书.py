#encoding:utf-8

import requests

url_baidu = 'https://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'}

response = requests.get(url_baidu,headers=headers,verify=False)
print(response.content.decode('utf-8'))