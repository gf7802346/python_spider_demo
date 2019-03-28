#encoding:utf-8

from bs4 import BeautifulSoup
from bs4.element import Tag

html = '''
<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48762&amp;keywords=&amp;tid=87&amp;lid=0">18796-数据分析师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48754&amp;keywords=&amp;tid=87&amp;lid=0">22090-兴趣阅读-推荐架构工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48749&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融云区块链高级研发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48751&amp;keywords=&amp;tid=87&amp;lid=0">31504-腾讯云大客户售后团队Leader/技术专家(上海/成都/深圳/北京)（深圳总部）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48752&amp;keywords=&amp;tid=87&amp;lid=0">22090-天天快报-数据开发工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48744&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融云互联网金融售前架构师（深圳/北京/上海）</a></td>
					<td>技术类</td>
					<td>4</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48745&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融售中架构师（大数据方向）（深圳/北京/上海）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48746&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融售中架构师（专有云方向）（深圳/北京/上海）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48739&amp;keywords=&amp;tid=87&amp;lid=0">28607-122 微信支付知识发现高级工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48743&amp;keywords=&amp;tid=87&amp;lid=0">29777-金融云保险行业售前架构师（深圳/北京/上海）</a></td>
					<td>技术类</td>
					<td>4</td>
					<td>深圳</td>
					<td>2019-03-21</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1451</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1450#a">146</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody>
<div>
我是文本
<div>
'''

soup = BeautifulSoup(html,'lxml')

# # 1.all tr
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
# #    print('#'*30)
#
# # 2.the second tr
# tr = soup.find_all('tr',limit=2)[1]
# # print(tr)
#
# # 3.class=even
# #trs = soup.find_all('tr',class_='even')
# trs = soup.find_all('tr',attrs={'class':'even'})
# for tr in trs:
# #    print(tr)
# #   print('#'*30)
#
# # 4.id=test class=test
# # aList = soup.find_all('a',attrs={'id':'test','class':'test'})
# # for a in aList:
# #     print(a)
#
# # 5.all a href
# aList = soup.find_all('a')
# for a in aList:
#     href = a['href']
# #    href = a.attrs['href']
#     print(href)
#
# # 6.all job
# trs = soup.find_all('tr')[1:]
# movies = []
# for tr in trs:
#     movie = {}
#     # 1.
#     # tds = tr.find_all('td')
#     # title = tds[0].string
#     # nums = tds[2].string
#     # movie['title'] = title
#     # movie['nums'] = nums
#     # movies.append(movie)
#
#     # 2.
#     infos = list(tr.stripped_strings)
#     movie['title'] = infos[0]
#     movie['nums'] = infos[2]
#     movies.append(movie)
#
# print(movies)

# aList = soup.find_all('a')
# for a in aList:
#     print(a['href'])

# bs4 4个常用对象
# from bs4.element import Tag
# from bs4.element import NavigableString
# from bs4.element import Comment
# from bs4 import BeautifulSoup
# contents 和 children

trs = soup.find('tr')
print(type(trs.contents))
for tr in trs.contents:
    print(tr)



