import requests
import os
import shutil
import re
import time
'''
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
'''
filename= 'novel1\\clear_address2.txt'
ospath= 'noel2\\'

with open(filename,encoding='utf-8')as f:

    i=0
    for line in f:
        url = line[0:44]
        title = line[45:75]
        print(url)
        print(title)

        response = requests.get(url)
        response.encoding = 'gbk'

        food = open('novel3\\%s str(title1).txt'%(int(i)+1),'a',encoding='utf-8')
        food.write(response.text)
        food.close()
        i=i+1

