#coding: utf-8

#http://www.renren.com/880151247/profile
#http://www.renren.com/PLogin.do

from urllib import request,parse
from http.cookiejar import CookieJar

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
# 1.获取cookie
cookiejar = CookieJar()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
# 2.登录主页
data = { 'email':'1130408003@qq.com','password':'7802346'}
login_url = "http://www.renren.com/PLogin.do"
req_login = request.Request(login_url,headers=headers,data=parse.urlencode(data).encode('utf-8'))
opener.open(req_login)
# 3.打开大鹏界面
dapeng_url = "http://www.renren.com/880151247/profile"
req_dapeng = request.Request(dapeng_url,headers=headers)
resp = opener.open(req_dapeng)
result = resp.read().decode('utf-8')
with open('dapeng.html','w',encoding='utf-8') as fp:
    fp.write(result)
