# coding=UTF-8
# Practice01-20200825
Balance = 2
emptySeet = 0
#while True:
if Balance > 1 :
    print ('Balance is enough,please check in!')
    Balance -= 1
    if emptySeet > 0 :
        emptySeet -= 1
        print ('Still have seats,please sit down!')
    else :
        print ('No seat left,please stand!')
else :
    print ('Balance is not enough,please top up!')



# Practice-20200826
# type()函数
a = 'It is a charactor.'
print (type ( a ))  # <type 'str'>
b = 1
print (type ( b ))  # <type 'int'>

# str()函数
c = str ( b )
d = c + 'funstrtest'
print (d)  # 1funstrtest

# int()函数
e = '3'
f = int ( e )
g = b + f
print (g)  # 4

# 列表list
class1 = [ 'A1', 'B2', 'C3', 'D4', 'E5' ]
for i in class1 :
    print (i)
a1 = [ 1, '123', [ 1, 2, 3 ] ]

# len()函数
l1 = len ( a1 )  # 3
print (l1)

# 列表切片，左闭右开
b1 = class1 [ 1 :4 ]
print (b1)  # ['B2', 'C3', 'D4']
c1 = class1 [ 1 : ]
print (c1)  # ['B2', 'C3', 'D4', 'E5']
d1 = class1 [ -3 : ]
print (d1)  # ['C3', 'D4', 'E5']
e1 = class1 [ :-2 ]
print (e1)  # ['A1', 'B2', 'C3']

# 添加列表元素 append()
score1 = [ ]
score1.append ( 6 )
print (score1)
score1.append ( 7 )
print (score1)

# 列表-->字符串 join()
tran1 = ';'.join ( class1 )
print (tran1)

# 字符串-->列表 split()
c2 = 'hello,world'
print (c2.split ( ',' ))

# 字典，键值对，冒号连接
class2 = {'k1' : 91, 'k2' : 92, 'k3' : 93, 'k4' : 94, 'k5' : 95}
score2 = class2 [ 'k2' ]  # 用键名提取键值
print (score2)
for i1 in class2 :
    print (i1 + ':' + str ( class2 [ i1 ] ))
a2 = class2.items()
print (a2)

#元组，类列表，元素不可修改 ()
class3 = ( 'A1', 'B2', 'C3', 'D4', 'E5' )
print (class3[1:3])

#集合，不重复数据 {}或set()
class4= [ 'A1','A1', 'B2', 'C3', 'D4', 'E5' ]
print (class4)
print (set(class4))  #未生效，可能是Python版本问题

for i2 in range(3):
    print (i2)

# Practice-20200827
try:
    print (1+'a')
except:
    print ('主代码执行失败')

#函数
def y(x):
    print (x+1)
y(10)

#str(int a)
#int(str s)
#len() 统计列表元素个数，字符串长度
title = ['t1','t2','t3']
print (len(title))
s1 = '12345我的家6789'  # 一个汉字3个字符
print (len(s1))         # 18

#replace(旧内容,新内容)  替换函数
w1 = '<em>今天是</em>投产日'
w1 = w1.replace('<em>','')
w1 = w1.replace('</em>','')
print (w1)

#strip() 删除空白字符（换行符\n和空格）
w2 = '    今天是\n周四'
w2 = w2.strip()
print (w2)     #空格删了，\n没成功

#split() 分割字符串，输出列表
d1 = '2020-08-27'
l2 = d1.split('-')
print (l2)
a3 = d1.split('-')[0]
print (a3)
print (l2[1])

#库
# import 库名
# from 库名 import 库里的一个功能
import time
print (time.strftime("%Y-%m-%d")) #2020-08-27

from datetime import datetime
print (datetime.now())   #2020-08-27 17:29:56.590000

import datetime
print (datetime.datetime.now())  #2020-08-27 17:29:56.590000

# Practice01-20200831
import re
content = 'Hello 123 world 456 for python_using 789'
result = re.findall('\d\d\d',content)
print(result)
aa = result[2]
print(aa)
# \d 匹配1个数字字符
# \w 匹配1个字母、数字或下划线字符
# \s 匹配1个空白字符，如换行符、制表符、普通空格等
# \S 匹配1个非空白字符
# \n 匹配1个换行符，相当于按1次Enter
# \t 匹配1个制表符，相当于按1次Tab或按8次空格键
# .  匹配1个任意字符，换行符除外
# *  匹配0个或多个表达式
# +  匹配1个或多个表达式
# ?  非贪婪限定符，常与.和*配合使用
# () 匹配括号内的表达式，也表示一个组

# (.*?)是要提取的内容
res1 = '文本A百度新闻文本B,文本A新浪新闻文本B,文本A网易新闻文本B'
p_source1 = '文本A(.*?)文本B'
source1 = re.findall(p_source1,res1)
print(source1)

# .*?是要忽视变化的内容
res2 = '文本A<变化的网址>文本C百度新闻文本B'
p_source2 = '文本A.*?文本C(.*?)文本B'
source2 = re.findall(p_source2,res2)
print(source2)

# Practice01-20200901
#<em>为标签,会自动跳过，输出为：['<em>阿里</em>代码AI评委能打分']
res3 = '<h3 class="c-title"><a href="网址"data-click="{英文&数字}"><em>阿里</em>代码AI评委能打分</a>'
p_source3 = '<h3 class="c-title">.*?>(.*?)</a>'
source3 = re.findall(p_source3,res3)
print(source3)
#sub()函数，替换
source3[0] = re.sub('<em>','',source3[0])
source3[0] = re.sub('</em>','',source3[0])
# source3[0] = re.sub('<.*?>','',source3[0])
print(source3)

#用re.S来忽略换行符进行匹配，'''框带换行符的内容，如下代码输出：['\n百度新闻']
res4 = '''文本A
百度新闻文本B'''
p_source4 = '文本A(.*?)文本B'
source4 = re.findall(p_source4,res4,re.S)
print(source4)
# strip函数去除空格或换行符，这里是去除\n 输出：['百度新闻']
# srtip(0)可以去除0，首位字符，中间的去不掉，如000123056000，去除后结果是123056
for i3 in range(len(source4)):
    source4[i3]=source4[i3].strip()
print(source4)

#[]，把特殊含义字符变成普通字符，如下*为特殊字符，要替换得用[]框起来
res5 = '*今天开学日'
source5 = re.sub('[*]','',res5)
print(source5)

# dir()函数
dir()

#import math

#set集合，去重
set1 = set([1,2,3,4,5,3,2,1])
print(set1)

#for... in...

