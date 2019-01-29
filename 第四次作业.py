# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:40:44 2019

@author: huyhui
@所有人
【Day 4】
判断语句（要求掌握多条件判断）
循环语句
三目表达式
容器
可迭代对象
迭代器
生成器
--------------------------------------
【作业构想】
学习代码200-300行
请对方输入一个0-9之间的数字，进行检查，若不是数字提示：您输入的不是数字，请输入0-9间的数字，若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。
系统随机生成一个长度为3的数字列表，且列表中元素在0-9之间并且不相等。将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，否则提示用户未得奖，输入1重新开始游戏，输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。
-------------------------------------
【作业提交时间】
2019年1月29日24：00
注意：未完成者将会被清退
------------------------------------
【点评】
完成时间：2019年1月30日12：00
注意：未完成竟会被清退
"""
#  判断和循环语句 
# if语句一般实例
if condition_1:
    statement_1
elif condition_2:
    statement_2
else:
    statement_3
'''如果 "condition_1" 为 True 将执行 "statement_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_2" 块语句
如果 "condition_2" 为False，将执行"statement_3"块语句'''     

gold = int(input("数学的分数："))
if gold < 60:
    print("不及格")
elif gold <= 70:
    print("合格")
elif gold <= 80:
    print("良")
else:
    print("优秀")
    
# if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小
# 于等于）来表示其关系。当判断条件为多个值时，可以使用以下形式：
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
num=0
if num==1:
    print("a")
elif num==2:
    print("b")
elif num==3:
    print("c")
else:
    print("hello")

## 循环语句
'''循环语句是在某种条件下，循环的执行某段代码块，并在符合条件的情况下跳出该段循环，
 其目的是处理想要进行处理的相同任务，关键词以for、while来标识。'''
 
# for循环语句
 #基本形式
for <variable> in <sequence>:
    statement_block_1
else:
    statement_block_2
    
# while循环语句
    # 基本形式 
while condition: 
    statement_block_1
else:
    statement_block_2

# break、continue、pass语句
while True:
    for i in range(10):
        if i < 5:
            print(i, ',', end='')
        elif i == 5:
            print('fifth', end='')
            continue
            print('This statement won\'t be executed!')
        else:
            pass
    break
# 输出结果  0 ,1 ,2 ,3 ,4 ,fifth

# 三目表达式
x = int(input("请输入第一数数:"))
y = int(input("请输入第二个数:"))
#一般的写法
if (x == y):
     print("两数相同！")
elif(x > y):
     print("较大的数为：",x)
else:
     print("较大的数为：",y)            
# 三目运算符写法
print(x if(x>y) else y)

# 容器
## 最常用的容器包括【列表】、【元组】、【字典】、【集合】

## 可迭代对象
'''像list、tuple可以通过for循环来遍历，这种遍历称为迭代(Iteration)，
这些可以直接作用于for循环对象统称为可迭代对象(Iterable)。但可迭代对
象不一定非得是基本数据结构，可以为任意对象，只要这个对象能返回一个迭
代器(iterator)。'''
from collections import Iterable
print('判断是否为可迭代对象：', isinstance('abc', Iterable))

x = 'abc'  # x为可迭代对象
y = iter(x)  # y为迭代器
for e in y:
    print(e)

#输出结果 
'''
判断是否为可迭代对象： True
a
b
c '''

## 生成器
L = [x * x for x in range(5)] #创建列表
G = (x * x for x in range(5)) #创建生成器
print(type(G))
for g in G:
    print(g, ' ', end='')

# 输出结果
# <class 'generator'>
#  0  1  4  9  16  

'''作业
请对方输入一个0-9之间的数字，进行检查，若不是数字
提示：您输入的不是数字，请输入0-9间的数字，若数字不在
0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。
系统随机生成一个长度为3的数字列表，且列表中元素在0-9之
间并且不相等。将用户输入与该列表进行比较，若为列表第一
个元素，则荣获第一名，列表第二个元素，则荣获第二名，列
表第三个名字，则荣获第三名，否则提示用户未得奖，输入1
重新开始游戏，输入2则结束游戏。注意：每次游戏中列表中
数字要求随机生成，每轮游戏都不相等。'''


import random
while True:
    num = input("请你输出一个数：")
    if num.isdigit():
        num = int(num)
        if num in range(10):
            break
        else:
            print("范围不再0-9之中，请输入0-9之间的数字")
    else:
        print("你输入的不是数字，请输入0-9之间的数字")
        continue
a = random.sample(range(0,9),3) #生成不相同的随机数
print(a)
if num==a[2]:
    print('荣获第三名')
elif num==a[1]:
    print('荣获第二名')
elif num==a[0]:
    print('荣获第三名')
else:
    print('未中奖')
    
'''输出结果：
请你输出一个数：2
[1, 4, 3]
未中奖

请你输出一个数：3
[8, 5, 6]
未中奖
    
请你输出一个数：3
[5, 0, 8]
未中奖


