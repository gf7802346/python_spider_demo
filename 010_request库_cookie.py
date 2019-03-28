#encoding:utf-8

import requests

url_baidu = 'https://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'}

response = requests.get(url_baidu,headers=headers)

print(response.cookies.get_dict)


url_profile = 'http://www.renren.com/880151247/profile'
url_login = 'http://www.renren.com/PLogin.do'
data = { 'email':'1130408003@qq.com','password':'7802346'}


session = requests.session()
session.post(url_login,headers=headers,data=data)
resp = session.get(url_profile)
print(resp.content.decode('utf-8'))

with open('request_cookie_dapeng.html','w',encoding='utf-8') as fp:
    fp.write(resp.content.decode('utf-8'))



