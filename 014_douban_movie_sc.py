#encoding: utf-8

import requests
from lxml import etree

# 1.下载页面
url = "https://movie.douban.com/cinema/nowplaying/xiangyang/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400",
    "Referer":"https://movie.douban.com/"
}

reponse = requests.get(url,headers=headers)
text = reponse.content.decode('utf-8')

# 2.提取数据
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
#print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = []
for li in lis:
    #print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    try:
        title = li.xpath("@data-title")[0]
        score = li.xpath("@data-score")[0]
        duration = li.xpath("@data-duration")[0]
        director = li.xpath("@data-director")[0]
        actors = li.xpath("@data-actors")[0]
        region = li.xpath("@data-region")[0]
        thumbnail = li.xpath(".//img/@src")[0]
        #print(thumbnail)
    except IndexError:
        pass
    movie = {
        "title":title,
        "score":score,
        "duration":duration,
        "director":director,
        "actors":actors,
        "region":region,
        "thumbnail":thumbnail
    }
    movies.append(movie)
print(movies)




