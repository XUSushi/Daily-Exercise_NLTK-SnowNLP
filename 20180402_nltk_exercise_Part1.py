# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 23:48:56 2018

@author: 许某某
"""
#
import nltk, re, pprint
from nltk import word_tokenize
#把nltk包引入
from urllib import request

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
#从上面这个网站的txt读内容进来
print(type(raw))#打印raw的数据类型
print(len(raw))#打印raw的数据类型
#print(raw[:75])

#注意文件开头行中的\r和\n 是Python显示特殊回车符和换行符的方式
print('---------------------------')
tokens = word_tokenize(raw)
#tokenize 将字符串分解为单词和标点符号，进而生成单词列表和标点符号。
print(type(tokens)) #使用word_tokenize，出来的是list

print(len(tokens))#分好后的类别长度
print(tokens[:10])#打印一部分看看效果
print('---------------------------')
text = nltk.Text(tokens)
print(type(text))
 #变成特殊形式的text了，nltk.text.Text
print(text[1024:1062])#打印一部分看看效果
text.collocations()
#nltk.collocations的功能是搭配研究		t-检验，卡方，点互信息

print('---------------------------')
print("找Part 1: ",raw.find("PART I"))#find()可以根据文本内容找到所在位置
print("找 End of Project Gutenberg's Crime: ",raw.rfind("End of Project Gutenberg's Crime"))
raw = raw[5338:1157743]
print(raw.find("PART I"))#在目标位置找特定内容位置





