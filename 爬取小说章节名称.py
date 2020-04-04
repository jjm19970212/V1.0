#加载头文件
import requests
import os
import shutil
import re

#创建文件
#filename = 'novel.txt'
#os.makedirs('novel2')
food = open('novel2.txt','a')
#请求头字典

#网页地址
url = 'https://www.shujy.com/5200/317078/'
#将获取的数据保存到变量中
response = requests.get(url)
#正则表达式匹配
#<a href="67419312.html">第1章 靳寒嵊玩女人很恐怖的</a>
reg = r'<a href="(.*?)">第(.*?)章 (.*?)</a>'
reg = re.compile(reg)
title = re.findall(reg)
print(reg)
#response.encoding = 'gbk'
#打印变量
print(response.text)
food.write(response.text)
food.write((title))
food.close()