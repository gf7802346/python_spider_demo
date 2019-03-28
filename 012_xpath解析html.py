#encoding: utf-8

from lxml import etree

text = '''
<div class="recommend-comp-city hide-recom dn" style="display: block;">
	<a rel="nofollow" href="javascript:;" class="expansion">展开<i></i></a>
    <div class="r_company_tit">推荐公司：</div>
    <ul class="r_company_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/9251.html">美柚</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1373.html">喜马拉雅fm</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/14229.html">微盟</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/49369.html">淘粉吧</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/107435.html">熊猫TV</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2768.html">易到用车</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/40738.html">小红唇</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/97631.html">汽车超人</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/109.html">蚂蜂窝</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/36996.html">三好网</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/4760.html">唯品会</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1686.html">爱奇艺</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23014.html">快法务</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1575.html">百度招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/81491.html">蚂蚁金服</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/62.html">今日头条</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2474.html">滴滴</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/20909.html">AcFun</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23489.html">点点客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/59251.html">映客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/3712.html">京东</a></li>
    	    </ul>
    <div class="r_city_tit">推荐城市：</div>
    <ul class="r_city_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都招聘</a></li>
    	    </ul>
</div>'''

def parse_text_file():
    '''
    解析规则html
    :return:
    '''
    html = etree.HTML(text)
    print(type(html))
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

def parse_lagou_file():
    '''
    解析不规则html
    :return:
    '''
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('lxml_lagou.html',parser=parser)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))


parse_text_file()
parse_lagou_file()