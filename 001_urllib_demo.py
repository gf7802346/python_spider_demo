#coding: utf-8
from urllib import request
resp = request.urlopen('http://www.baidu.com')
request.urlretrieve('http://www.baidu.com','baidu.html')


from urllib import parse
params = {'name':'峰峰'}
print(parse.urlencode(params))

wd = {'wd':'杨幂','性别':'女'}
url = 'https://www.baidu.com/s'+'?'+parse.urlencode(wd)
print(request.urlopen(url))
print(parse.parse_qs(parse.urlencode(wd)))
print(parse.urlparse(url))
print(parse.urlparse(url).scheme)




