import sys
from fake_useragent import UserAgent
ua = UserAgent()
with open('UserAgent.txt','w+') as fp:
    flag = 0
    num = 10000
    while flag < num:
        fp.write(ua.random + '\n')
        fp.flush()
        flag += 1
        percent = flag / num
        pr = str(sys.stdout.write("%.1f" % (percent * 100))) + '%'
        print(pr)

    fp.close()
    print('已完成:%d个'%flag)
