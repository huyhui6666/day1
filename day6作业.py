# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:07:10 2019

@author: huyhui

【Day 6】
函数关键字
函数的定义
函数参数与作用域
函数返回值
【鉴于第五天内容较难，第6天内容减少，请同学们自行补充第五天知识体系】
--------------------------------------
【作业构想】
实现random.sample方法
实现Max方法
实现判断两个字符串是否相等的方法
-------------------------------------
【作业提交时间】
2019年1月31日24：00
注意：未完成者将会被清退
------------------------------------
【点评】
完成时间：2019年2月1日12：00
注意：未完成竟会被清退
"""

#  作业 实现random.sample方法
import random
list = [1,2,3,4,5,6,7,8,9,10,10]
for i in range(6):
    slice = random.sample(list,5)
    print(slice)
    print(list, '\n')

'''输出结果：
发现每一次的random.sample函数返回的5个元素不同
[4, 7, 6, 9, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 

[1, 5, 6, 4, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 

[2, 3, 8, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 

[10, 6, 3, 10, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 

[1, 7, 2, 8, 5]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 

[6, 2, 3, 7, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10] 
'''
# 函数的定义
'''函数是组织好的，可重复使用的，用来
实现单一或相关联功能的代码段。函数能
提高应用的模块性，和代码的重复利用率。

基本形式：
def function_name(param1, parma2, param3, **kwargs):
      statement_block
      return function_result

'''
'''
函数返回值
用def语句创建函数时，可以用 return 语句指定应该返回什么值。(没有return的函数即默认return None)

return 语句包含以下部分：

return 关键字
函数应该返回的值或表达式
'''
def func():
    print('Hello everyone!')
    
result = func()
print(result is None)

# 输出结果
'''
Hello everyone!
True
'''

# 作业 实现Max方法
def big(a,b,c):
    # 先比较a和b
    if a > b:
        maxnum = a
    else:
        maxnum = b
    if c > maxnum:
        maxnum = c
    else:
        c =maxnum
    return maxnum
a1=int(input('请输入一个数：'))
b1=int(input('请输入一个数：'))
c1=int(input('请输入一个数：'))
maxnum = big(a1,b1,c1)
print("最大的数是：",maxnum)

"""
请输入一个数：2

请输入一个数：3

请输入一个数：4
最大的数是： 4
"""

# 作业 实现判断两个字符串是否相等的方法
def comparison(a,b):
    ib=0
    for ia in range(len(a)):
        if ord(a[ia:ia+1])-ord(b[ib:ib+1])==0:
            ib=ib+1
            if ib==len(b):
                print('a and b are equall')
        else:
            print('a and b are not equall')
            break
n=input('请输入第一个字符串：')
m=input('请输入第二个字符串：')
comparison(m,n)

"""输出结果：
请输入第一个字符串：1

请输入第二个字符串：2
a and b are not equall

输出结果：

请输入第一个字符串：sd

请输入第二个字符串：sd
a and b are equall
"""



    



