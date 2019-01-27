# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:18:26 2019

@author: huyhui
"""
"""
@所有人
【Day 2】
基础
列表
标志
基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
列表相关方法
元组
标志
基本操作（创建及不可变性）
提升
序列类型，相互转换及方法
【作业构想】
学习代码200-300行
定义一个列表，包含自己的家庭成员，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
----------------------------------------------------------------
【作业提交】
1.代码文件链接分享到群
截至日期：2019年1月27日晚22：00
注意：未完成将被清退
------------------------------------------------------------------ 
【点评】
第一天点评截止时间1月27晚12点
注意：未完成将被清退
"""
#  -------列表------
# 创建一个列表，只要把逗号分隔的不同数据项使用方括号括起来就行
number = [1, 2, 3, 4, 5, 6] #普通列表创建
mix = [1 , 'ab', [1, 2, 3], 2.1] #混合列表创建
empty = [] #空列表创建

print('number[1]:', number[1]) #输出列表的第二个
print(number[0:]) #输出整个列表数据
print(mix[0:2]) # 输出前三个

# 向列表中添加一个元素方法
list = [] # 创建一个空列
list.append(1)
print('list=',list) #向空列表中添加一个元素 list= [1] 

# 向列表中添加多个元素的方法
list = [1, 2, 4] #创建一个列表
list.extend([2, 1, 4, "s"]) 
print('list = ', list) #向列表中添加多个元素

# 从列表中获取元素
name = ['哈登', '保罗', '卡佩拉', '周琦']
name[0] # '哈登'
name[3] # '周琦'
# 将哈登和周琦换位置
name[0], name[3] = name[3], name[0]
name #输出结果 ['周琦', '保罗', '卡佩拉', '哈登']

# 从列表中删除元素 有三种方式 remove()、del、pop()
#remove()
list = [1, 2, 3, 4, 5, 6] #创建一个列表
list.remove(1)  #这个方法只能删除一个
list #输出结果 [2, 3, 4, 5, 6]
#del
list = [1, 2, 3, 4, 5, 6] #创建一个列表
del list[0] # 删除一个元素
list #输出结果 [2, 3, 4, 5, 6]
del list[:] # 删除整个列表中的元素
del list[:3] # 删除第1,2,3个元素
list # [4, 5, 6]
# pop()
list = [1, 2, 3, 4, 5, 6] #创建一个列表
list.pop()
list # 输出结果 [1, 2, 3, 4, 5] 可知pop()默认删除最后一个元素
list.pop(1)
list # 输出结果 [1, 3, 4, 5] 也可以指定相应的元素

# 列表分片与反转
list = [1, 2, 3, 4, 5, 6] #创建一个列表
list[0:2] #输出结果是 [1, 2]
list[0:6:2] #输出结果是 [1, 3, 5] 每前进两个元素才取出来一个
list[::2] #输出结果是 [1, 3, 5] 与list[0:6:2]是一样的
list[::-1] #输出结果是  [6, 5, 4, 3, 2, 1] 反转
list[::-2] #输出结果[6, 4, 2]

# 操作符
list1 = [123]
list2 = [234]
list1 > list2 #输出结果 False

list1 = ['abs']
list2 = ['bcz']
list1 < list2  #输出结果 True

# 列表相加
list1 = [123]
list2 = [234]
list3 = list1 + list2
list3 #输出结果  [123, 234] 其中+运算是指的

# 列表相乘为复制
list1 = [123]
list1 *= 3
list1 # 输出结果[123, 123, 123]

#in 和 not in 操作
list = [1, 2, 3, 4,[5, 6], 1] #创建一个列表
0 in list # 输出结果 False
1 in list #输出结果  True
list[4][0] #输出结果 5

list.count(1) #统计下1出现的次数
list.index(1) #查找参数的位置

list.reverse() #翻转
list #输出结果[1, [5, 6], 4, 3, 2, 1]

list = [2, 4, 6, 5, 9, 1, 0, 7, 8]
list.sort() #列表排序
list  #输出结果[0, 1, 2, 4, 5, 6, 7, 8, 9]
# 序列类型包括字符串类型、列表类型、元组类型
# 
# (1)list转换为string或tuple
li = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
sli = str(li)
print(sli)
tli = tuple(li)
print(tli)

# (2)string转换为lsit或tuple
s = 'hello, world!'
ls = list(s)
print(ls)
ls1 = s.split(',')
print(ls1)
ts = tuple(s)
print(ts)

# (3)tuple转换成string或list
tu = (1, 2, 3, 4, 'a', 'b', 'c', 'd')
stu = str(tu)
print(stu)
ltu = list(tu)
print(ltu)

'''元组'''
# 创建元组
tuple = (1, 2, 3, 4, 5, 6, 7 ,8)
#访问元组 
tuple[1] # 输出结果2
tuple[:2] # 输出结果(1, 2)
#元组中最重要的是逗号，一定主要需要逗号
8*(8) #输出为64
8*(8,)   #输出为(8, 8, 8, 8, 8, 8, 8, 8)

# 1.2.3 元组运算符
len((1, 2, 3))  # 计算元素个数
(1, 2, 3) + (4, 5, 6)  # 连接
('Hi!',) * 4  # 复制
3 in (1, 2, 3)  #元素是否存在
for x in (1, 2, 3): 
print (x,)　　# 迭代 

#更新和删除元组
# 注意：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (1, 2, 3)
tup2 = ('test1', 'test2', 'test3')
tup3 = tup1 + tup2
print(tup3)

# 遍历
ser_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in ser_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in favorite_languages.keys():
    print(name.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 第二次作业
my_home = ['mine', 'father', 'mother', 'sister', 'brother']
print(my_home)
my_home.append('girlfriend')
print(my_home)
my_home.insert(2,'boyfriend')
print(my_home)
my_home.pop()
print(my_home)
my_home.pop(2)
print(my_home)

#作业输出结果
#['mine', 'father', 'mother', 'sister', 'brother']
#['mine', 'father', 'mother', 'sister', 'brother', 'girlfriend']
#['mine', 'father', 'boyfriend', 'mother', 'sister', 'brother', 'girlfriend']
#['mine', 'father', 'boyfriend', 'mother', 'sister', 'brother']
#['mine', 'father', 'mother', 'sister', 'brother']







