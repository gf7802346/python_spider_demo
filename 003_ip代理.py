#coding: utf-8

from urllib import request,parse
import re

#没使用代理
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print('没使用代理:'+str(resp.read()))

#使用代理
handler = request.ProxyHandler({'http':'123.127.93.188:44399'})
opener = request.build_opener(handler)
resp = opener.open(url)
print('使用代理:'+str(resp.read()))