#coding: utf-8

#http://www.renren.com/880151247/profile

from urllib import request,parse

#没有cookie
url = "http://www.renren.com/880151247/profile"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Cookie':'Cookie: anonymid=jsycfjd5l65bax; depovince=ZGQT; jebecookies=62bf9001-b648-427b-861b-51b88b84818f|||||; _r01_=1; JSESSIONID=abcaYpwPgUr_45GlolxLw; ick_login=eb1ecf4b-db11-4a14-b713-dfd3fe15c327; _de=BEB7A92F74453A9CDBA4353CE6B34778; p=3507283e66a23b9636ba92674a35e9531; ap=821959761; first_login_flag=1; ln_uact=15527226179; ln_hurl=http://head.xiaonei.com/photos/0/0/women_main.gif; t=3750201620676461d2698df5d42e3d911; societyguester=3750201620676461d2698df5d42e3d911; id=821959761; xnsid=a8d2c6f2; ver=7.0; loginfrom=null; jebe_key=102d9eed-eec8-4a81-8f0d-9e57688d8804%7C8d01a2ba241522c80e5986599d473023%7C1551945776489%7C1%7C1551945774623; wp_fold=0'}
rep = request.Request(url=url,headers=header)
resp = request.urlopen(rep)
resu = resp.read().decode('utf-8')
print(resu)
with open ('renren.html','w',encoding='utf-8') as fp:
    fp .write(resu)
    fp.close()

#youcookie