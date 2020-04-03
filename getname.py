#todo 使用到的库文件
import  requests
import threading
from bs4 import BeautifulSoup
import re
import os
import time
'''
requests：用于get请求
threading：多线程
bs4：网页解析
re：正则表达式
os：系统相关操作
time：获取时间
'''

#TODO 2.对网页文件结构进行分析（PS：浏览器使用的是谷歌浏览器）
#TODO请求头字典3.获取网页的请求头文件
req_header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'__cfduid=d577ccecf4016421b5e2375c5b446d74c1499765327; UM_distinctid=15d30fac6beb80-0bdcc291c89c17-9383666-13c680-15d30fac6bfa28; CNZZDATA1261736110=1277741675-1499763139-null%7C1499763139; tanwanhf_9821=1; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1499612614,1499672399,1499761334,1499765328; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1499765328; tanwanpf_9817=1; bdshare_firstime=1499765328088',
'Host':'www.qu.la',
'Proxy-Connection':'keep-alive',
'Referer':'http://www.qu.la/book/1265/765108.html',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
'''
我们需要的是第二个方框中的内容（Request Headers），
将该目录下的信息取出，存放到字典中，其中每一个项所代表的意义如果感兴趣可自行网上搜索（HTTP Header 详解）。
'''

#TODO4.分析每章小说网页结构
