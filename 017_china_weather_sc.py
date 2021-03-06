#encoding:utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar
import random
ALL_DATA = []

def parse_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    reponse = requests.get(url,headers=headers)
    text = reponse.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    result = []
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index==0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city':city,'min_temp':int(min_temp)})
    return ALL_DATA
def main():
    urls = [
     'http://www.weather.com.cn/textFC/hb.shtml',
     'http://www.weather.com.cn/textFC/db.shtml',
     'http://www.weather.com.cn/textFC/hz.shtml',
     'http://www.weather.com.cn/textFC/hn.shtml',
     'http://www.weather.com.cn/textFC/xb.shtml',
     'http://www.weather.com.cn/textFC/xn.shtml',
     'http://www.weather.com.cn/textFC/gat.shtml'
    ]

    for url in urls:
        result = parse_page(url)
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    print(ALL_DATA)
    with open('weather.txt','w+',encoding='utf-8') as fp:
        fp.write(str(ALL_DATA))
    data = ALL_DATA
    #data = [{'city': '呼伦贝尔', 'min_temp': -18}, {'city': '大兴安岭', 'min_temp': -12}, {'city': '黑河', 'min_temp': -9}, {'city': '果洛', 'min_temp': -9}, {'city': '伊春', 'min_temp': -8}, {'city': '海北', 'min_temp': -8}, {'city': '那曲', 'min_temp': -8}, {'city': '阿里', 'min_temp': -8}, {'city': '锡林郭勒', 'min_temp': -7}, {'city': '兴安盟', 'min_temp': -7}, {'city': '白城', 'min_temp': -7}, {'city': '辽源', 'min_temp': -7}, {'city': '白山', 'min_temp': -7}, {'city': '阜新', 'min_temp': -7}, {'city': '甘南', 'min_temp': -7}, {'city': '齐齐哈尔', 'min_temp': -6}, {'city': '牡丹江', 'min_temp': -6}, {'city': '大庆', 'min_temp': -6}, {'city': '鹤岗', 'min_temp': -6}, {'city': '长春', 'min_temp': -6}, {'city': '松原', 'min_temp': -6}, {'city': '抚顺', 'min_temp': -6}, {'city': '大同', 'min_temp': -5}, {'city': '包头', 'min_temp': -5}, {'city': '乌兰察布', 'min_temp': -5}, {'city': '哈尔滨', 'min_temp': -5}, {'city': '绥化', 'min_temp': -5}, {'city': '鸡西', 'min_temp': -5}, {'city': '吉林', 'min_temp': -5}, {'city': '四平', 'min_temp': -5}, {'city': '玉树', 'min_temp': -5}, {'city': '山南', 'min_temp': -5}, {'city': '通辽', 'min_temp': -4}, {'city': '赤峰', 'min_temp': -4}, {'city': '佳木斯', 'min_temp': -4}, {'city': '延边', 'min_temp': -4}, {'city': '通化', 'min_temp': -4}, {'city': '阿勒泰', 'min_temp': -4}, {'city': '北屯', 'min_temp': -4}, {'city': '双河', 'min_temp': -4}, {'city': '海南', 'min_temp': -4}, {'city': '海西', 'min_temp': -4}, {'city': '朔州', 'min_temp': -3}, {'city': '七台河', 'min_temp': -3}, {'city': '双鸭山', 'min_temp': -3}, {'city': '铁岭', 'min_temp': -3}, {'city': '延安', 'min_temp': -3}, {'city': '张掖', 'min_temp': -3}, {'city': '阿坝', 'min_temp': -3}, {'city': '呼和浩特', 'min_temp': -2}, {'city': '沈阳', 'min_temp': -2}, {'city': '本溪', 'min_temp': -2}, {'city': '朝阳', 'min_temp': -2}, {'city': '西宁', 'min_temp': -2}, {'city': '海东', 'min_temp': -2}, {'city': '甘孜', 'min_temp': -2}, {'city': '迪庆', 'min_temp': -2}, {'city': '昌都', 'min_temp': -2}, {'city': '乌海', 'min_temp': -1}, {'city': '辽阳', 'min_temp': -1}, {'city': '定西', 'min_temp': -1}, {'city': '延庆', 'min_temp': 0}, {'city': '密云', 'min_temp': 0}, {'city': '张家口', 'min_temp': 0}, {'city': '承德', 'min_temp': 0}, {'city': '太原', 'min_temp': 0}, {'city': '晋中', 'min_temp': 0}, {'city': '吕梁', 'min_temp': 0}, {'city': '巴彦淖尔', 'min_temp': 0}, {'city': '丹东', 'min_temp': 0}, {'city': '锦州', 'min_temp': 0}, {'city': '葫芦岛', 'min_temp': 0}, {'city': '金昌', 'min_temp': 0}, {'city': '临夏', 'min_temp': 0}, {'city': '阿拉尔', 'min_temp': 0}, {'city': '黄南', 'min_temp': 0}, {'city': '石嘴山', 'min_temp': 0}, {'city': '固原', 'min_temp': 0}, {'city': '日喀则', 'min_temp': 0}, {'city': '忻州', 'min_temp': 1}, {'city': '盘锦', 'min_temp': 1}, {'city': '榆林', 'min_temp': 1}, {'city': '武威', 'min_temp': 1}, {'city': '塔城', 'min_temp': 1}, {'city': '银川', 'min_temp': 1}, {'city': '吴忠', 'min_temp': 1}, {'city': '中卫', 'min_temp': 1}, {'city': '拉萨', 'min_temp': 1}, {'city': '怀柔', 'min_temp': 2}, {'city': '平谷', 'min_temp': 2}, {'city': '宝坻', 'min_temp': 2}, {'city': '蓟州', 'min_temp': 2}, {'city': '阿拉善盟', 'min_temp': 2}, {'city': '鞍山', 'min_temp': 2}, {'city': '营口', 'min_temp': 2}, {'city': '酒泉', 'min_temp': 2}, {'city': '白银', 'min_temp': 2}, {'city': '嘉峪关', 'min_temp': 2}, {'city': '昌吉', 'min_temp': 2}, {'city': '博尔塔拉', 'min_temp': 2}, {'city': '通州', 'min_temp': 3}, {'city': '武清', 'min_temp': 3}, {'city': '北辰', 'min_temp': 3}, {'city': '唐山', 'min_temp': 3}, {'city': '阳泉', 'min_temp': 3}, {'city': '长治', 'min_temp': 3}, {'city': '鄂尔多斯', 'min_temp': 3}, {'city': '平凉', 'min_temp': 3}, {'city': '乌鲁木齐', 'min_temp': 3}, {'city': '石河子', 'min_temp': 3}, {'city': '阿克苏', 'min_temp': 3}, {'city': '伊犁', 'min_temp': 3}, {'city': '图木舒克', 'min_temp': 3}, {'city': '五家渠', 'min_temp': 3}, {'city': '林芝', 'min_temp': 3}, {'city': '海淀', 'min_temp': 4}, {'city': '朝阳', 'min_temp': 4}, {'city': '石景山', 'min_temp': 4}, {'city': '大兴', 'min_temp': 4}, {'city': '房山', 'min_temp': 4}, {'city': '东城', 'min_temp': 4}, {'city': '西城', 'min_temp': 4}, {'city': '滨海新区', 'min_temp': 4}, {'city': '秦皇岛', 'min_temp': 4}, {'city': '运城', 'min_temp': 4}, {'city': '神农架', 'min_temp': 4}, {'city': '商洛', 'min_temp': 4}, {'city': '哈密', 'min_temp': 4}, {'city': '可克达拉', 'min_temp': 4}, {'city': '北京', 'min_temp': 5}, {'city': '顺义', 'min_temp': 5}, {'city': '昌平', 'min_temp': 5}, {'city': '丰台', 'min_temp': 5}, {'city': '门头沟', 'min_temp': 5}, {'city': '保定', 'min_temp': 5}, {'city': '廊坊', 'min_temp': 5}, {'city': '雄安新区', 'min_temp': 5}, {'city': '晋城', 'min_temp': 5}, {'city': '大连', 'min_temp': 5}, {'city': '鹤壁', 'min_temp': 5}, {'city': '济源', 'min_temp': 5}, {'city': '兰州', 'min_temp': 5}, {'city': '天水', 'min_temp': 5}, {'city': '克拉玛依', 'min_temp': 5}, {'city': '巴音郭楞', 'min_temp': 5}, {'city': '喀什', 'min_temp': 5}, {'city': '铁门关', 'min_temp': 5}, {'city': '丽江', 'min_temp': 5}, {'city': '宁河', 'min_temp': 6}, {'city': '衡水', 'min_temp': 6}, {'city': '临汾', 'min_temp': 6}, {'city': '随州', 'min_temp': 6}, {'city': '杨凌', 'min_temp': 6}, {'city': '庆阳', 'min_temp': 6}, {'city': '昭通', 'min_temp': 6}, {'city': '西青', 'min_temp': 7}, {'city': '静海', 'min_temp': 7}, {'city': '津南', 'min_temp': 7}, {'city': '武汉', 'min_temp': 7}, {'city': '仙桃', 'min_temp': 7}, {'city': '潜江', 'min_temp': 7}, {'city': '新乡', 'min_temp': 7}, {'city': '南阳', 'min_temp': 7}, {'city': '濮阳', 'min_temp': 7}, {'city': '三门峡', 'min_temp': 7}, {'city': '铜川', 'min_temp': 7}, {'city': '克州', 'min_temp': 7}, {'city': '天津', 'min_temp': 8}, {'city': '东丽', 'min_temp': 8}, {'city': '和平', 'min_temp': 8}, {'city': '河东', 'min_temp': 8}, {'city': '河西', 'min_temp': 8}, {'city': '南开', 'min_temp': 8}, {'city': '河北', 'min_temp': 8}, {'city': '红桥', 'min_temp': 8}, {'city': '邯郸', 'min_temp': 8}, {'city': '孝感', 'min_temp': 8}, {'city': '咸宁', 'min_temp': 8}, {'city': '长沙', 'min_temp': 8}, {'city': '益阳', 'min_temp': 8}, {'city': '商丘', 'min_temp': 8}, {'city': '漯河', 'min_temp': 8}, {'city': '西安', 'min_temp': 8}, {'city': '咸阳', 'min_temp': 8}, {'city': '渭南', 'min_temp': 8}, {'city': '汉中', 'min_temp': 8}, {'city': '广元', 'min_temp': 8}, {'city': '黔江', 'min_temp': 8}, {'city': '城口', 'min_temp': 8}, {'city': '酉阳', 'min_temp': 8}, {'city': '秀山', 'min_temp': 8}, {'city': '毕节', 'min_temp': 8}, {'city': '大理', 'min_temp': 8}, {'city': '石家庄', 'min_temp': 9}, {'city': '黄冈', 'min_temp': 9}, {'city': '黄石', 'min_temp': 9}, {'city': '荆州', 'min_temp': 9}, {'city': '恩施', 'min_temp': 9}, {'city': '天门', 'min_temp': 9}, {'city': '湘潭', 'min_temp': 9}, {'city': '株洲', 'min_temp': 9}, {'city': '常德', 'min_temp': 9}, {'city': '郑州', 'min_temp': 9}, {'city': '安阳', 'min_temp': 9}, {'city': '驻马店', 'min_temp': 9}, {'city': '安康', 'min_temp': 9}, {'city': '宝鸡', 'min_temp': 9}, {'city': '陇南', 'min_temp': 9}, {'city': '和田', 'min_temp': 9}, {'city': '巴中', 'min_temp': 9}, {'city': '垫江', 'min_temp': 9}, {'city': '梁平', 'min_temp': 9}, {'city': '石柱', 'min_temp': 9}, {'city': '六盘水', 'min_temp': 9}, {'city': '昆明', 'min_temp': 9}, {'city': '沧州', 'min_temp': 10}, {'city': '邢台', 'min_temp': 10}, {'city': '襄阳', 'min_temp': 10}, {'city': '鄂州', 'min_temp': 10}, {'city': '宜昌', 'min_temp': 10}, {'city': '十堰', 'min_temp': 10}, {'city': '荆门', 'min_temp': 10}, {'city': '娄底', 'min_temp': 10}, {'city': '岳阳', 'min_temp': 10}, {'city': '张家界', 'min_temp': 10}, {'city': '湘西', 'min_temp': 10}, {'city': '许昌', 'min_temp': 10}, {'city': '平顶山', 'min_temp': 10}, {'city': '开封', 'min_temp': 10}, {'city': '洛阳', 'min_temp': 10}, {'city': '绵阳', 'min_temp': 10}, {'city': '内江', 'min_temp': 10}, {'city': '雅安', 'min_temp': 10}, {'city': '云阳', 'min_temp': 10}, {'city': '巫山', 'min_temp': 10}, {'city': '忠县', 'min_temp': 10}, {'city': '安顺', 'min_temp': 10}, {'city': '黔东南', 'min_temp': 10}, {'city': '曲靖', 'min_temp': 10}, {'city': '保山', 'min_temp': 10}, {'city': '邵阳', 'min_temp': 11}, {'city': '怀化', 'min_temp': 11}, {'city': '焦作', 'min_temp': 11}, {'city': '周口', 'min_temp': 11}, {'city': '吐鲁番', 'min_temp': 11}, {'city': '成都', 'min_temp': 11}, {'city': '南充', 'min_temp': 11}, {'city': '达州', 'min_temp': 11}, {'city': '遂宁', 'min_temp': 11}, {'city': '资阳', 'min_temp': 11}, {'city': '眉山', 'min_temp': 11}, {'city': '凉山', 'min_temp': 11}, {'city': '德阳', 'min_temp': 11}, {'city': '南川', 'min_temp': 11}, {'city': '巴南', 'min_temp': 11}, {'city': '万州', 'min_temp': 11}, {'city': '巫溪', 'min_temp': 11}, {'city': '大足', 'min_temp': 11}, {'city': '武隆', 'min_temp': 11}, {'city': '綦江', 'min_temp': 11}, {'city': '遵义', 'min_temp': 11}, {'city': '铜仁', 'min_temp': 11}, {'city': '黔西南', 'min_temp': 11}, {'city': '衡阳', 'min_temp': 12}, {'city': '郴州', 'min_temp': 12}, {'city': '永州', 'min_temp': 12}, {'city': '信阳', 'min_temp': 12}, {'city': '来宾', 'min_temp': 12}, {'city': '贺州', 'min_temp': 12}, {'city': '自贡', 'min_temp': 12}, {'city': '泸州', 'min_temp': 12}, {'city': '宜宾', 'min_temp': 12}, {'city': '乐山', 'min_temp': 12}, {'city': '合川', 'min_temp': 12}, {'city': '渝北', 'min_temp': 12}, {'city': '北碚', 'min_temp': 12}, {'city': '长寿', 'min_temp': 12}, {'city': '涪陵', 'min_temp': 12}, {'city': '奉节', 'min_temp': 12}, {'city': '潼南', 'min_temp': 12}, {'city': '荣昌', 'min_temp': 12}, {'city': '铜梁', 'min_temp': 12}, {'city': '彭水', 'min_temp': 12}, {'city': '开州', 'min_temp': 12}, {'city': '黔南', 'min_temp': 12}, {'city': '玉溪', 'min_temp': 12}, {'city': '临沧', 'min_temp': 12}, {'city': '德宏', 'min_temp': 12}, {'city': '玉林', 'min_temp': 13}, {'city': '广安', 'min_temp': 13}, {'city': '重庆', 'min_temp': 13}, {'city': '永川', 'min_temp': 13}, {'city': '江津', 'min_temp': 13}, {'city': '渝中', 'min_temp': 13}, {'city': '璧山', 'min_temp': 13}, {'city': '丰都', 'min_temp': 13}, {'city': '大渡口', 'min_temp': 13}, {'city': '江北', 'min_temp': 13}, {'city': '沙坪坝', 'min_temp': 13}, {'city': '九龙坡', 'min_temp': 13}, {'city': '南岸', 'min_temp': 13}, {'city': '贵阳', 'min_temp': 13}, {'city': '文山', 'min_temp': 13}, {'city': '楚雄', 'min_temp': 13}, {'city': '柳州', 'min_temp': 14}, {'city': '桂林', 'min_temp': 14}, {'city': '梧州', 'min_temp': 14}, {'city': '河池', 'min_temp': 14}, {'city': '韶关', 'min_temp': 14}, {'city': '梅州', 'min_temp': 14}, {'city': '河源', 'min_temp': 14}, {'city': '云浮', 'min_temp': 14}, {'city': '潮州', 'min_temp': 14}, {'city': '南宁', 'min_temp': 15}, {'city': '崇左', 'min_temp': 15}, {'city': '贵港', 'min_temp': 15}, {'city': '钦州', 'min_temp': 15}, {'city': '防城港', 'min_temp': 15}, {'city': '佛山', 'min_temp': 15}, {'city': '肇庆', 'min_temp': 15}, {'city': '揭阳', 'min_temp': 15}, {'city': '攀枝花', 'min_temp': 15}, {'city': '普洱', 'min_temp': 15}, {'city': '台北', 'min_temp': 15}, {'city': '北海', 'min_temp': 16}, {'city': '广州', 'min_temp': 16}, {'city': '惠州', 'min_temp': 16}, {'city': '珠海', 'min_temp': 16}, {'city': '清远', 'min_temp': 16}, {'city': '东莞', 'min_temp': 16}, {'city': '中山', 'min_temp': 16}, {'city': '百色', 'min_temp': 17}, {'city': '汕头', 'min_temp': 17}, {'city': '江门', 'min_temp': 17}, {'city': '阳江', 'min_temp': 17}, {'city': '汕尾', 'min_temp': 17}, {'city': '红河', 'min_temp': 17}, {'city': '怒江', 'min_temp': 17}, {'city': '西双版纳', 'min_temp': 17}, {'city': '澳门', 'min_temp': 17}, {'city': '台中', 'min_temp': 17}, {'city': '深圳', 'min_temp': 18}, {'city': '湛江', 'min_temp': 18}, {'city': '茂名', 'min_temp': 18}, {'city': '香港', 'min_temp': 19}, {'city': '白沙', 'min_temp': 20}, {'city': '五指山', 'min_temp': 20}, {'city': '高雄', 'min_temp': 20}, {'city': '临高', 'min_temp': 21}, {'city': '澄迈', 'min_temp': 21}, {'city': '儋州', 'min_temp': 21}, {'city': '昌江', 'min_temp': 21}, {'city': '琼中', 'min_temp': 21}, {'city': '乐东', 'min_temp': 21}, {'city': '屯昌', 'min_temp': 22}, {'city': '文昌', 'min_temp': 22}, {'city': '保亭', 'min_temp': 22}, {'city': '海口', 'min_temp': 23}, {'city': '东方', 'min_temp': 23}, {'city': '定安', 'min_temp': 23}, {'city': '琼海', 'min_temp': 23}, {'city': '万宁', 'min_temp': 23}, {'city': '陵水', 'min_temp': 23}, {'city': '三亚', 'min_temp': 24}, {'city': '西沙', 'min_temp': 26}, {'city': '中沙', 'min_temp': 27}, {'city': '南沙', 'min_temp': 27}]
    cities = list(map(lambda x:x['city'],data))
    temps = list(map(lambda x: x['min_temp'], data))
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart = Bar('柱状图')
    chart.add(
        "",
        cities,
        temps,
        v1,
        is_datazoom_show=True,
        datazoom_type="both",
        datazoom_range=[10, 25],
    )
    #chart.add('',cities,temps)
    chart.render('tempture.html')


if __name__ == '__main__':
    # 排序
    # DATA = [
    #     {'city':'beijing','min_temp':10},
    #     {'city': 'tianjin', 'min_temp': -8},
    #     {'city': 'shanghai', 'min_temp': -10}
    # ]
    # DATA.sort(key=lambda data:data['min_temp'])
    # print(DATA)

    main()