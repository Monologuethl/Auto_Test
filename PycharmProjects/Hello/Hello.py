# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# def nop():
#     pass
#
# list =[1,2,3]
# for x in  list:
#     print(x)
#
# print(my_abs(-2)
# )
# import math
# print(math.sqrt(2))
# for i,value in enumerate(['a','b','c']):
#     print(i,value)
# list=list(range(1,11))
# for i in list:
#     print(i)
#
# list=[x * x for x in range(1, 11)]
# print(list)
#
# def fib (max):
#     n ,a ,b =0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#         return n
#
# print(fib(9))
#
# def triangles():
#     result=[1]
#     n=0
#     while n<10:
#         print(result)
#         tem=result[:]
#         result.append(1)
#         for x in range(1,len(result)-1):
#             result[x]=tem[x-1]+tem[x]
#         n=n+1
#
# triangles()
# def f(x):
#     return x * x
#
# print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# def normalize(name):
#     return(name[0].upper() + name[1:].lower())
# print(list(map(normalize,['adam','liZa'])))
#
# def str2num(str):
#         DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}
#         return DIGITS[str]
#
#     def fn(x, y):
#         return x  10 + y
#     def power(a, b = 0.1):
#         s = 1
#         while a > 0:
#             a = a - 1
#             s = s  b
#         return s
#     n = 0
#     for c in list(map(str2num, s)):
#         n = n + 1
#         if c < 0:
#             break
#     return reduce(fn, map(str2num, s[:(n-1)])) + reduce(fn, map(str2num, s[n:]))*power(len(s)-n)
# from functools import reduce
#
# CHAR_TO_INT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9
# }
#
# def str2int(s):
#     ints = map(lambda ch: CHAR_TO_INT[ch], s)
#     return reduce(lambda x, y: x * 10 + y, ints)
#
# print(str2int('0'))
# print(str2int('12300'))
# print(str2int('0012345'))
#
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
#
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)
#
# print(str2float('0'))
# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))
#
# def main():
#     for n in primes():
#         if n < 1000:
#             print(n)
#         else:
#             break
#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
# if __name__ == '__main__':
#     main()
# def is_palindrome(i):
#     i = str(i)
#     return i[::1] == i[::-1]
#
# print(list(filter(is_palindrome,range(1,200))))
# def by_name(t):
#     print(t[0])
#     return t[0]
#
# def by_score(t):
#     return t[1]
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print(L2)
#
# L3 = sorted(L, key=by_score)
# print(L3)
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ' a test module '
#
# __author__ = 'Michael Liao'
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()
# def _private_1(name):
#     return 'Hello, %s' % name
#
# def _private_2(name):
#     return 'Hi, %s' % name
#
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
# class Student(object):


#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# class MyObject(object):
#      def __init__(self):
#         self.x=9
#         def power(self):
#              return self.x*self.x
#
# obj =MyObject()
# print(hasattr(obj,'x'))
# print(obj.x)
# setattr(obj,'y',19)
# print(getattr(obj,'y'))
# class Student(object):
#     pass
# s=Student()
# s.name='Miachael'
# print(s.name)
# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s.set_age=MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
#
# def set_score(self,score):
#     self.score=score
# Student.set_score=set_score
#
# s.set_score(100)
# print(s.score)
# class Student(object):
#     __slots__ = ('name','age')
#
# s=Student()
# s.name='Michael'
# s.age=25
#
# class GranduatesStudent(Student):
#     pass
#
# g=GranduatesStudent()
# g.score=9999
# print(g.score)
#
# class Student(object):
#     @property
#     def get_score(self):
#         return  self.score
#     # @score.setter
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("scoe must be integer!")
#         if value<0 or value>100:
#             raise ValueError("score must bettwen 0~100")
#         self.score=value
# s=Student()
# # s.set_score(60)
# # print(s.get_score())
# s.score=60
# print(s.score)
# import os
#
# def strFind(rootDir,text):
#     for fileName in os.listdir(rootDir):
#         fileDir = os.path.join(rootDir,fileName)
#         if os.path.isfile(fileDir):
#             if text in fileName:
#                 print(os.path.relpath(fileName,fileDir))
#         elif os.path.isdir(fileDir):
#             for fileName1 in os.listdir(fileDir):
#                 fileDir1 = os.path.join(fileDir,fileName1)
#                 if text in fileName1:
#                     print(os.path.relpath(fileName1,fileDir1))
#         else:
#             print('error:%s' %fileName)
#
# Dir,text = input('please input dir and text:').split()
#
# st = strFind(Dir,text)
# import time
# words = input('Please input the words you want to say!:')
# for item in words.split():
#     print('\n'.join([''.join([(item[(x-y) % len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(12, -12, -1)]))
#     time.sleep(1.5);
# os.system('clear')
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
# -*- coding: utf-8 -*-
# import hashlib, random
#
# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
# def login(username, password):
#     user = db[username]
#     return user.password == get_md5(password)
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')
# from urllib import request, parse
#
# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))
# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# -*- coding:utf-8 -*-
#
# from xml.parsers.expat import ParserCreate
# from urllib import request
#
# class DefaultSaxHandler(object):
#     weather = {'forecast': []}
#     def start_element(self, name, attrs):
#         if name == 'yweather:location':
#             self.weather['city'] = attrs['city']
#         elif name == 'yweather:forecast':
#             self.weather['forecast'].append({
#                     'date': attrs['date'],
#                     'high': attrs['high'],
#                     'low': attrs['low']
#                 })
#
# def parseXml(xml_str):
#     handler = DefaultSaxHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.Parse(xml_str)
#     return handler.weather
#
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
#
# with request.urlopen(URL, timeout=4) as f:
#     data = f.read()
#
# result = parseXml(data.decode('utf-8'))
# assert result['city'] == 'Beijing'
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 16:03
# @Author  : john fan
# @Email   : jianlongfan@gmail.com
# @File    : ex_HTMLPASER_2.py
# @Software: PyCharm
#
# from html.parser import HTMLParser
# from html.entities import name2codepoint
# from urllib import request
# import re
#
#
# class MyHTMLParser(HTMLParser):
#     a_t1 = False
#     a_t2 = False
#     a_t3 = False
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.information = []
#         self.information_all = {}
#
#
#     def handle_starttag(self, tag, attrs):
#         def _attr(attrlist, attrname):
#             for attr in attrlist:
#                 if attr[0] == attrname:
#                     return attr[1]
#             return None
#
#         if tag=="time" :
#             self.a_t1 = True
#         elif tag=="span" and _attr(attrs, 'class')=="event-location":
#             self.a_t2 = True
#         elif tag=="h3" and _attr(attrs, 'class')=="event-title":
#             self.a_t3 = True
#
#
#     def handle_data(self, data):
#         if self.a_t1 is True:
#             if re.match(r'^\s\d{4}', data):
#                 self.information.append(dict(year=data))
#             else:
#                 self.information.append(dict(day=data))
#         elif self.a_t2 is True:
#             self.information.append(dict(event_location=data))
#         elif self.a_t3 is True:
#             self.information.append(dict(event_title=data))
#
#
#     def handle_endtag(self, tag):
#         if tag == "time":
#             self.a_t1 = False
#         elif tag =="span":
#             self.a_t2 = False
#         elif tag == "h3":
#             self.a_t3 = False
#
#
#
# def parseHTML(html_str):
#     parser = MyHTMLParser()
#     parser.feed(html_str)
#     for i, val in enumerate(parser.information):
#         i +=  1
#         print(val)
#         if i%4==0:
#
#             print('--------------------------------------------')
#
#
# URL = 'https://www.python.org/events/python-events/'
# with request.urlopen(URL, timeout=4) as f:
#     data = f.read()
#
# parseHTML(data.decode('utf-8'))
