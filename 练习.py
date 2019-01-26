# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:12:24 2019

@author: huyhui
"""
"""python初体验
print and input
---------------------------
python基础讲解
python变量特性+命名规则
注释方法
python中“：”作用
学会使用dir( )及和help( )
import使用
pep8介绍
---------------------------
python数值基本知识
python中数值类型，int，float，bool，e记法等
算数运算符
逻辑运算符
成员运算符
身份运算符
运算符优先级
---------------------------
string字符串
定义及基本操作（+，*，读取方式）
字符串相关方法
字符串格式化问题"""

# 练习
print("hello the world")
name = input("你的姓名是：")

# 运算符法则


 #模块导入import 主要有以下四种调用方式
import time    #这是直接调用time模块中的函数
from time import time  #这种事从time模块中调用os函数，
from time import *  #这种方式是用*来导入模块中所有的命名空间； 
import time as y    #利用这种方法给导入的命名空间替换一个新的名字

'''
Python成员运算符
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''
a = 40
b = 2
list = [1, 2, 3, 4, 5 ]; 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中") 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中") 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")
   
"""
python身份运算符
"""
"""类型转换 
 int()作用是将一个字符串或浮点数转换为一个整数
 """
a = '250'
c = 5.77 
b = int(a)
print(b)
d = int(c)
print(d)
"""float()的作用是将一个字符串或整数转换成一个浮点数（就是小数）"""
a = '232'
b = float(a)
c = 52
d = float(c)
"""str()的作用是将一个数或其他类型转换成一个字符串"""
a = 5.7
b = str(a)

# 字符串 
a = "Hello"
b = "World"
 
print("a + b 输出结果：", a + b)
print("a * 3 输出结果：", a * 3)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')

"""身份运算符"""
a = 5
b = 5
if(a is b):
 print("1-a和b有相同的标识")
else:
 print("1-a和b没有相同的标识")
#改变a的值
a=7
b=4
if(a is not b):
 print("2-a和b没有相同的标识")
else:
 print("2-a和b有相同的标识")

"""上面的输出结果
1-a和b有相同的标识
2-a和b没有相同的标识"""
   
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#字符串复制
s1 = 'hello the world'
s2 = s1          # s2 = 'hello the world'
#若指定长度
s1 = 'hello'
s2 = s1[0:2]     #s2 = 'he'

#字符串比较 
'''
（1）利用operator模块方法比较（python3.X取消了cmd函数）
包含的方法有：
lt(a, b) ———— 小于
le(a, b) ———— 小于等于
eq(a, b) ———— 等于
ne(a, b) ———— 不等于
ge(a, b) ———— 大于等于
gt(a, b) ———— 大于
'''
import operator
operator.eq('abc','edf') #根据ASCII码比较
operator.gt('abc','ab')
 
#（2）关系运算符比较（>,<,>=,<=,==,!=）
s1 = 'abc'
s2 = 'ab'
s1 > s2
s1 == s2

#字符串翻转
s1 = 'hello the world'
s2=s1[::-1]
print(s1)
print(s2)

'''
字符串内查找 
find方法：
检测字符串内是否包含子串str
语法为：
    str.find(str[,start,end])
    str为要查找的字符串；
    strat为查找起始位置，默认为0；
    end为查找终止位置，默认为字符串长度。
    若找到返回起始位置索引，否则返回-1
 '''

s1 = 'today is a fine day'
s1.find('is')       
s1.find('is',3)
s1.find('is',7,10)

'''
字符串内替换 
replace方法：
把字符串中的旧串替换成新串
语法为：
    str.replace(old,new[,max]) #old为旧串，new为新串，max可选，为替换次数
'''
s1 = 'today is a find day'
print(s1)
s2=s1.replace('find','rainy')
print(s2)

# 作业 
#法一 最简单的input和print函数的书写

name = input("输入姓名：")
age = input("输入年龄：")
sex = input("输入性别：")
print('您的姓名是：%s，您的性别是：%s，您是%d年出生的人'%(name,sex,2019-int(age))) 












