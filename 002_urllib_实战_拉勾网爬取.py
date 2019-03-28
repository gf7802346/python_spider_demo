#coding: utf-8

from urllib import request,parse

url = 'https://www.lagou.com/jobs/companyAjax.json?needAddtionalResult=false'
resp = request.urlopen(url)
print(resp.read())
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36","Referer":"https://www.lagou.com/",
           "Referer":"https://www.lagou.com/jobs/list_java?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=?labelWords=hot"
           }
data = {'first':'true','pn':1,'kd':'java'}

rep = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(rep)
print(resp.read().decode("utf-8"))
