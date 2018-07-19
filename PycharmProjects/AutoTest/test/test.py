# import json
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data)
# print ("Python 原始数据：", repr(data))
# print ("JSON 对象：", json_str)

import time;  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

import time

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
