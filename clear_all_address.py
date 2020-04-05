#http://www.freesion.com/article/757572535/
# -*- coding:utf-8
import re
import os
import shelve


#文件地址
filename = 'address\\get_address_all.txt'
with open(filename) as f:
    contents = f.read()
#打印contents内容
#print(contents)
content1=re.findall('<title>(.*?)</title>',contents)
#<dd><a href="66689436.html" title="第1章 靳寒嵊玩女人很恐怖的">第1章 靳寒嵊玩女人很恐怖的</a> </dd>
content2 = re.findall('<dd><a href=(.*?)</a> </dd>',contents)
content3 = re.findall('<dd><a href="(.*?)"',contents)
content4 = re.findall('<dd><a href="(.*?)" title="(.*?)">(.*?)</a> </dd>',contents)
print(content1)
print(content2)
print(content3)
print(content4)

#fw=open('novel1\\clear_address.txt','a',encoding='utf-8')
#fw.write('\n'.join('{} {}'.format(x[0],x[1])for x in content4))
#fw.close()
#shelffile


fq=open('novel1\\clear_address1.txt','a',encoding='utf-8')
fq.write('\n'.join('{} {}'.format(x[0],x[1])for x in content4))
fq.close()
