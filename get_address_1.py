#http://www.freesion.com/article/757572535/
#https://www.xs321.com/18/18812/66689436.html
# -*- coding:utf-8
import re
import os
import shelve

f2=open('novel1\\clear_address2.txt','a',encoding='utf-8')
#文件地址
filename = 'novel1\\clear_address.txt'
with open(filename,encoding='utf-8') as file:
    for line in file:

        print("https://www.xs321.com/18/18812/"+line)
        f2.write('https://www.xs321.com/18/18812/'+line)

f2.close()