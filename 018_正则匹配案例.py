#encoding: utf-8

import re

# 1.验证手机号码
text= '15527226179'
ret = re.match('1[34578]\d{9}',text)
print(ret.group())

# 2.验证邮箱
text = '1130408003@qq.com'
ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
print(ret.group())

# 3.验证url
text = 'http://www.baidu.com'
ret = re.match('(http|https|ftp)://[^\s]+',text)
print(ret.group())

# 4.验证身份证
text = '42062152421254652X'
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())

# 5.^() or [^] 以xxx开头
text = 'hello'
#ret = re.match('[^\s]+',text)
ret = re.match('^he',text)
print(ret.group())

# 6.以xxx结尾
text = 'hello@163.com'
ret = re.match('\w+@163.com$',text)
print(ret.group())

# 7.匹配多个字符或者表达式
text = 'https'
ret = re.match('(http|https|ftp)$',text)
print(ret.group())

# 8.贪婪模式与非贪婪模式
text = 'hello'
ret = re.match('^he',text)
print(ret.group())















