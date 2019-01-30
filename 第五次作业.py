'''@所有人
【Day 5】
正则表达式re
os模块
datetime模块
http请求
--------------------------------------
【作业构想】
请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。
对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地
-------------------------------------
【作业提交时间】
2019年1月30日24：00
注意：未完成者将会被清退
------------------------------------
【点评】
完成时间：2019年1月31日12：00
注意：未完成竟会被清退'''

## 正则表达式re
  # compile()
import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))   #查找所有包含'oo'的单词
# 输出结果 ['good', 'cool'] 
  # match()

# urllib提供了一系列用于操作URL的功能
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',data.decode('utf-8'))

from urllib import request
req=request.Request("http://www.douban.com/")
req.add_header('User-Agent','Mozilla/6.0(iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',f.read().decode('utf-8'))



# post请求
import urllib
import json

url = 'http://www.daily.com/ABC/ABC/ABC'
values = {
            "abc":"XXXXX",
            "efg":"XXXXX"
            }

headers = {'Content-Type': 'application/json'} # 设置请求头 告诉服务器请求携带的是json格式的数据
request = urllib.request.Request(url=url, headers=headers, data=json.dumps(values).encode(encoding='UTF8')) # 需要通过encode设置编码 要不会报错

response = urllib.request.urlopen(request) # 发送请求

logInfo = response.read().decode() # 读取对象 将返回的二进制数据转成string类型
print(logInfo)


#get请求
import urllib

# get请求
resu = urllib.request.urlopen('https://hao.360.cn', data=None, timeout=10)
data = resu.read().decode()

#打开文件
fo = open('test.txt','a+',encoding = 'utf-8') # 打开文件 这里网络数据流的编码需要和写入的文件编码一致
fo.write(data)   # 写入文件
fo.close()       # 关闭文件

##datetime模块
# datetime是Python处理日期和时间的标准库。
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
2019-01-30 16:28:07.198690
print(type(now))
<class 'datetime.datetime'>
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
如果仅导入import datetime，则必须引用全名datetime.datetime。
datetime.now()返回当前日期和时间，其类型是datetime。

#http请求
'''
import requests
from requests.auth import HTTPBasicAuth
response = requests.post('http://localhost:8080/jenkins/job/check_python_version/build',auth=('admin','wangmin'))
print (response.status_code)
print (response.reason)
print(response.headers)
'''
'''
###作业 请用户输入一个时间，输出选项所对应的现在时间，
# 告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。对
http://www.baidu.com 进行请求，并用正则化匹配图片内容。
将百度图标爬取下来保存至本地'''
import datetime
str=input('请输入一个时间（时间的格式为年，月，日，小时，分钟，秒）：')
data=datetime.strptime(str,'%Y-%M-%D %H:%M:%S')
now=datetime.now()
diff=now.timestamp()-_date.timestamp()
# print(diff) #得到相差的秒数
print("现在离输入的时间相差%d天，%d时，%d分，%d秒"%(diff/(24*3600),diff%(24*3600)/3600,diff%3600/60,diff%60))

###
import re
telephone=input("请输入您的电话：")
resNum=re.match(r'^1[3,4,5,6,7,8]\d{9}$',telephone)
if resNum:
    print("输入的电话合法")
else:
    print("输入电话号码不合法")
email=input("请输入邮箱：")
resEmail=re.compile(r'^[a-zA-Z0-9_][a-zA-Z0-\_\-\.]+@[a-zA-Z0-9]+\.[com,cn,net]{1,3}$')
if resEmail.match(email):
    print(email)
else:
    print("输入的邮箱不合法")

'''###http://www.baidu.com 进行请求，并用正则化匹配图片内容。
#将百度图标爬取下来保存至本地'''
from urllib import request
with request.urlopen('http://www.baidu.com') as f:
    data=f.read()
    print("Status:",f.status,f.reason)
    buf=data.decode('utf-8')
    img=r'src="(.+?\.png)"'
    imglist=re.findall(img,buf)
    for addr in imglist:
        print(addr)
        request.urlretrieve("https:"+addr,r"Y:\logo.png")