#encoding: utf-8

from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('lxml_tencent.html',parser=parser)

i=1

print(str(i)*50)
i+=1
# 1.获取tr标签
trs_all = html.xpath('//tr')
for tr in trs_all:
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

print(str(i)*50)
i+=1
# 2.获取第二个tr标签
print(html.xpath('//tr[2]')[0])

print(str(i)*50)
i+=1
# 3.获取tr标签中class=even的标签
tr_class_even = html.xpath("//tr[@class='even']")
for tr in tr_class_even:
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

print(str(i)*50)
i+=1
# 4.获取a标签的href属性
a_all = html.xpath("//a/@href")
for a in a_all:
    print("https://hr.tencent.com/"+a)

print(str(i)*50)
i+=1
# 5.获取所有职位信息
tr_alljob = html.xpath("//tr[position()>1]")
positions = []
for tr in tr_alljob:
    try:
        href = tr.xpath(".//a/@href")[0]
        fullurl = "https://hr.tencent.com/"+href
        #title = tr.xpath(".//a/text()")[0]
        title = tr.xpath("./td[1]//text()")[0]
        category = tr.xpath("./td[2]/text()")[0]
        nums = tr.xpath("./td[3]/text()")[0]
        adress = tr.xpath("./td[4]/text()")[0]
        pubtime = tr.xpath("./td[5]/text()")[0]
    except IndexError:
        pass
    position = {
        'url':fullurl,
        'title':title,
        'category':category,
        'nums':nums,
        'adress':adress,
        'pubtime':pubtime
    }
    positions.append(position)

print(positions)















