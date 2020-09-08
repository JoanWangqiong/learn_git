import requests
import re
from bs4 import BeautifulSoup as bs
#bs4是库，BeautifulSoup是包

#模拟浏览器登录
user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
header = {'User-Agent':user_agent}

myurl = 'https://movie.douban.com/top250'
res = requests.get(myurl,headers=header).text
#print(res)
bs_info = bs(res,'html.parser')

for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a',):
        #获取所有链接，1）使用attrs，属性为class，值为hd的，2）链接的开头是a
        print(atag.get('href'))
        #获取第一个span，find函数默认第一个，find_all是所有
        print(atag.find('span',).text)




