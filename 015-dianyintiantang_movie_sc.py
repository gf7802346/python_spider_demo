#encoding:utf-8

import requests
from lxml import etree

DOMAIN = "https://www.dytt8.net"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400",
        "Referer": "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
    }


def get_detail_urls(url):
    reponse = requests.get(url, headers=HEADERS)
    text = reponse.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:DOMAIN+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    movie = {}
    reponse = requests.get(url,headers=HEADERS)
    text = reponse.content.decode('gbk')
    html = etree.HTML(text)

    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    images = zoomE.xpath(".//img/@src")
    cover = images[0]
    screenshot = images[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,'').strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        elif info.startswith("◎视频尺寸"):
            info = parse_info(info,"◎视频尺寸")
            movie['size'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                movie['profile'] = profile

    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url

    return movie


def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for x in range(1,8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)
    print(movies)


spider()



















