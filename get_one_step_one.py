import requests
import os
import shutil
import re

food = open('novel2\\get_address_all.txt','a',encoding='utf-8')
#请求头字典

#网页地址
url = 'https://www.xs321.com/18/18812/66689436.html'
#将获取的数据保存到变量中
response = requests.get(url)
response.encoding = 'gbk'



#打印变量
print(response.text)
food.write(response.text)

food.close()