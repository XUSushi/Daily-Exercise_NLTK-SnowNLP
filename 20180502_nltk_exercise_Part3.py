
# coding: utf-8


# In[1]:

#Looking up lemmas and synonyms in WordNet
#在wordnet中查找lemma和同义词


# In[2]:

##方法一


# In[3]:

from nltk.corpus import wordnet as wn


# In[9]:

wn.synset('car.n.01').lemma_names()
#python 3与2有区别，结果不会有u前缀


# In[6]:

u'motorcar'.encode('utf-8')#有一个u 前缀表示它是Unicode字符串


# In[7]:

##方法二


# In[8]:

a = wn.synset('car.n.01').lemma_names()
#lemma_names()函数可以看lemma的名字
print (a)


# In[11]:

wn.synset('car.n.01').definition ()
#查看定义/解释


# In[12]:

#Calculating WordNet synset similarity
#计算wordNet中synset相似度


# In[13]:

##量度一：path_similarity--基于上位词层次结构中相互连接的概念之间的最短路径在0-1之间打分
#（两者之间没有路径返回-1，与自身比较返回1）


# In[14]:

from nltk.corpus import wordnet as wn

right = wn.synset('right_whale.n.01')

minke = wn.synset('minke_whale.n.01')
#设置好两个synset

right.path_similarity(minke)
#path_similarity()函数，基于上位词层次结构中相互连接的概念之间的最短路径


# In[15]:

##量度二：wup_similarity 
#wup_similarity 是 Wu-Palmer Similarity 的简称
#它是一种评分方法，它基于单词感知的相似程度以及在高级树中互相之间作用的位置


# In[16]:

from nltk.corpus import wordnet

cb = wordnet.synset('cookbook.n.01')

ib = wordnet.synset('instruction_book.n.01')
#设置好两个synset

cb.wup_similarity(ib)
#wup_similarity()函数


# In[17]:

#Discovering word collocations (relative to n-gram)


# In[18]:

#发掘单词搭配（基于n-gram）


# In[22]:

from nltk import bigrams

a = "Jaganadh is testing this application"
#待分析的句子
tokens = a.split()
#分词
bigrams(tokens)
#看词汇搭配bigrams()


# In[23]:

#这里出现了和教材不一样的地方，打印bigrams(token)不会出现两两词的列表


# In[24]:

#查资料发现是没变成列表的原因，改成下面这样


# In[25]:

v=bigrams(tokens)


# In[27]:

list(v)
#打印出的结果：
"""
[('Jaganadh', 'is'),
 ('is', 'testing'),
 ('testing', 'this'),
 ('this', 'application')]
"""


# In[29]:

#如果已经分词则
list(bigrams(['more', 'is', 'said', 'than', 'done']))


# In[30]:

##词频统计


# In[32]:

from nltk.book import text1
'''
*** Introductory Examples for the NLTK Book ***

Loading text1, ..., text9 and sent1, ..., sent9

Type the name of the text or sentence to view it.

Type: 'texts()' or 'sents()' to list the materials.

text1: Moby Dick by Herman Melville 1851

text2: Sense and Sensibility by Jane Austen 1811

text3: The Book of Genesis

text4: Inaugural Address Corpus

text5: Chat Corpus

text6: Monty Python and the Holy Grail

text7: Wall Street Journal

text8: Personals Corpus

text9: The Man Who Was Thursday by G . K . Chesterton 1908
'''


# In[33]:

from nltk import FreqDist


# In[35]:

fdist1 = FreqDist(text1)#词和词频


# In[36]:

print(fdist1)


# In[37]:

fdist1


# In[38]:

fdist1.most_common(50)#最多的50个


# In[39]:

# 绘制累积频率图


# In[40]:

import matplotlib


# In[ ]:

fdist1.plot(50, cumulative=True)


# In[ ]:

#绘图出来了，会弹出一个窗口，另存为图片


# In[ ]:



