#https://www.xs321.com/18/18812/66689436.html

import os
from requests_html import HTMLSession
session = HTMLSession()

filename= 'novel1\\clear_address2.txt'
ospath= 'noel2\\'

with open(filename,encoding='utf-8')as f:

    i=0
    for line in f:
        url = line[0:44]
        titlea = line[45:75]
        print(url)
        print(titlea)
        r = session.get(url)
        title = r.html.find('body > div > div > div.yd_text2', first=True)
        # r.html.find() 接受一个 CSS 选择器（字符串形式）作为参数
        # 返回在网页中使用该选择器选中的内容。

        #print(title.text)
        f = open('novel2\\名门影后.txt', 'a', encoding='utf-8')
        f.write(titlea + '\n'+title.text+'\n\n\n')
        f.close()


        i=i+1