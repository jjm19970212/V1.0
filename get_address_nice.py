#http://www.freesion.com/article/757572535/
#https://www.xs321.com/18/18812/66689436.html
# -*- coding:utf-8
import re
import os
import shelve

filename = 'novel1\\clear_address2.txt'
address=open('novel1\\address.txt','a',encoding='utf-8')
title =open('novel1\\title.txt','a',encoding='utf-8')
with open(filename,encoding='utf-8')as f:
    for line in f:
        print(line[0:44])
        address.write(line[0:44]+'\n')
        title.write(line[45:70])

address.close()
title.close()