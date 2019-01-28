# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:49:01 2019

@author: huyhui

所有人
【Day 3】
【dict字典】
定义
创建
字典的相关方法
-----------------------------------
【set集合】
特性
创建
方法
-------------------------------------
【file文件读取】
 打开文件方式（读写两种方式）
文件对象的操作方法
*学习对excel及csv文件进行操作*
**内容为选做内容，可根据自己基础决定是否做此内容
--------------------------------------
【作业构想】
学习代码200-300行
读取一个文件【文件将在之后给出】，将文件中转换为字典，key值为学习项目，value值为一个负责人列表，并判断字典中是否有负责人负责多个学习项目。
-------------------------------------
【作业提交时间】
2019年1月28日24：00
注意：未完成者将会被清退
------------------------------------
【点评】
完成时间：2019年1月29日12：00
注意：未完成竟会被清退
"""


'字典'
# 定义 字典是python中唯一的映射类型，映射在数学上是一个术语，指两个元素之间的对应关系

# 字典是由key and value 构成，无序结构（不想列表那样有固体位置）
d = {key1 : value1, key2 : value2 } #键必须是唯一，但值则不必
dict = {'a' : 1, 'b' : 2, 'b' : 3}
dict['b'] #输出结果 3 
dict #输出结果  {'a': 1, 'b': 3} 
#上面的例子可知 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。


dict1 = {                    # 由等式构成 dict = { “key” : "value,....}
    "sid170" : "hbb",        # :不能写成“=” ; 结束要有 “,”.
    'sid171' : "zheng",
    'tid' : {                # 嵌套 "key1" : {"key" : "value"}
     "tid01" : "wang",
     'tid02' : "deng"
}                            # 总体而言需要注意：1）何时用等号，何时用冒号；2）记得加逗号
}

# 访问字典里的值
dict = {'name': 'paul','b': 9,'class': 'second'}
print("dict['name']:", dict['name'])
print("dict['b']:", dict['b'])

#上面输出为
# dict['name']: paul
# dict['b']: 9

# 修改字典的值
dict = {'name': 'paul','b': 9,'class': 'second'}
dict['b'] = 10 #更新 b
dict['home'] = "小甲鱼" #添加信息
print("dict['b']:", dict['b'])
print("dict['home']:",dict['home'])
#输出结果为
# dict['b']: 10
# dict['home']: 小甲鱼

# 删除字典元素
dict = {'name': 'paul','b': 9,'class': 'second'}
del dict['name'] #删除键 ‘name’
dict.clear() # 清空字典
del dict #删除字典

# set集合
# 集合是一个无序且不重复的元素集合，定义方式类似于字典
set={'a','b','c','a','b','d','f','cd'}#创建集合
print(set)
#运行结果：
# {'d', 'cd', 'b', 'c', 'f', 'a'}

set.add('haden')#添加元素
print(set)
#运行结果：
#{'d', 'haden', 'cd', 'b', 'c', 'f', 'a'}

set.clear()#清空所有元素
print(set)
#运行结果：
#set()

set={'name','age','gender'}
set1=set.copy() #浅拷贝
print(set1)
运行结果：
{'name', 'gender', 'age'}

set1={'python','java','big data'}
set2={'java','c','c++'}
set3=set1.difference(set2) #返回由两个或多个set中不同的元素组成一个新set
print(set3)
运行结果：
{'big data', 'python'}

#set.discard 删除指定元素,元素不存在不报错
set1={'python','java','big data','ML'}
set2=set1.discard('python')
print(set1)
#运行结果：
#{'java', 'ML', 'big data'}

#set.pop 随机指定集合元素可赋值其他容器（占位符）
	set1={'python','java','big data','ML'}
	set2=set1.pop()
	print(set2)
#	运行结果：
#	java
set.intersection返回两个或多个set的交集，即两个或多个set中都存在的元素组成的set
set.isdisjoint 如果两个set没有交集，返回true
set.issubset 判断A集合是否是B集合的子集。
set.issupreset 判断A集合是否是B集合的父集。
set.symmetric_difference 返回A集合和B集合的差集
set.union 返回A集合和B集合的并集

# file文件
# Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
open(file,mode='r')

# 完整语法
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

#打开一个文件
f = open("xxx.txt","r")
str = f.read(1)
print("读取的字符串是：", str)
f.close() #关闭打开的文件

# 读取一个文件，将文件中转换为字典，key值为学习项目，value值为一个负责人列表，并判断字典中是否有负责人负责多个学习项目。



dict1={}#建立空字典
names=[]
with open('E:\homework.txt',encoding='UTF-8')as f:#读取文件
    for line in f.readlines():
        word=line.strip()#去除\n
        key=word.split()[0]#提取key值
        value=[word.split()[1],word.split()[2]]#提取value值
        dict1[key]=value
names=[key,value]
print(dict1)
for key in dict1:
    for i in range(2):
        for key2 in dict1:
            for j in range(2):
                if dict1[key][i]==dict1[key2][j]:
                    cn=1;
if cn==1:
    print("有重复")
