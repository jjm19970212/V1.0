#加载头文件
import requests
import os
import shutil
#创建文件
#filename = 'novel.txt'
os.makedirs('novel1')
food = open('novel1.txt','w')
#请求头字典

#网页地址
url = 'https://www.shujy.com/5200/317078/'
#将获取的数据保存到变量中
response = requests.get(url)
#response.encoding = 'gbk'
#打印变量
print(response.text)
food.write(response.text)
food.close()
'''
title=re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
fb=open('%s.txt'% title,'w',encoding='utf-8')
with open(filename,'w') as file:
    file.write(html)
file.close()
#请求下载
'''















































































































