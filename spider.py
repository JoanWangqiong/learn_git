import requests
import re
from bs4 import BeautifulSoup as bs
#bs4是库，BeautifulSoup是包
import lxml.etree

def get_url_name(myurl):
    #模拟浏览器登录
    user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    header = {'User-Agent':user_agent}

    #myurl = 'https://movie.douban.com/top250'
    res = requests.get(myurl,headers=header).text
    #print(res)
    bs_info = bs(res,'html.parser')

    for tags in bs_info.find_all('div',attrs={'class':'hd'}):
        for atag in tags.find_all('a',):
            #获取所有链接，1）使用attrs，属性为class，值为hd的，2）链接的开头是a
            print(atag.get('href'))
            #获取第一个span，find函数默认第一个，find_all是所有
            print(atag.find('span',).text)

#生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
print(urls)

#控制请求的频率，引入time模块
from time import sleep
sleep(10)

for page in urls
    get_url_name(page)
    sleep(5)

url = 'https://movie.douban.com/subject/1292052'
user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
header = {'User-Agent':user_agent}
response = requests.get(url,headers=header)

#xml化处理
selector = lxml.etree.HTML(response.text)

#获取电影名称，在F12界面上，选中对应块，直接copy Xpath
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')

#上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

# 评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分:{rating}')

mylist = [film_name,plan_date,rating]

import pandas as pd

movie1 = pd.DataFrame(data = mylist)
movie1.to_csv('./movie1.csv',encoding='gbk',index=False,header=False)

