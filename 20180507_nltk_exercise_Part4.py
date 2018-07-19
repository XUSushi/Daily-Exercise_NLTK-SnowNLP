
# coding: utf-8

# In[1]:

#Stemming words
#提取词根/词干


# In[2]:

#单个词


# In[3]:

from nltk.stem import PorterStemmer # "Poter"是一种词干提取的算法。


# In[4]:

stemmer = PorterStemmer()


# In[5]:

stemmer.stem('cooking')


# In[6]:

stemmer.stem('cookery')


# In[7]:

#返回的值不一定是个有效单词，比如这个结果是‘cookeri’,这不是出错了。


# In[8]:

#多个词


# In[9]:

import nltk


# In[10]:

stemmer = nltk.PorterStemmer()


# In[11]:

verbs = ['appears', 'appear', 'appeared', 'calling', 'called']


# In[12]:

stems = []


# In[13]:

for verb in verbs:
    #遍历
    stemmed_verb = stemmer.stem(verb)
    #把每个词都处理放进stems中
    stems.append(stemmed_verb) # 一定要按两次回车键，然后再输入下面的语句。
    
    


# In[14]:

sorted(set(stems))#抽取多个词的词干


# In[15]:

#Lemmatizing words with WordNet
#用wordnet来把单词变体还原


# In[16]:

from nltk.stem import WordNetLemmatizer


# In[17]:

lemmatizer = WordNetLemmatizer()


# In[21]:

lemmatizer.lemmatize('cooking')
#没有提供pos的话，就默认还原为名词（n)


# In[19]:

lemmatizer.lemmatize('cooking', pos='v')#pos设定还原的词性，为动词


# In[27]:

lemmatizer.lemmatize('better', pos='a')#变成形容词


# In[28]:

#Replacing words matching regular expressions
#替换与正则表达式匹配的单词


# In[31]:

#分为两步
"""
STEP1:在本地新建一个文件，里面存储替换的内容和替换操作函数。放在python的lib下
STEP2:运行这个文件，进行替换操作
"""


# In[30]:

from replacers import RegexpReplacer


# In[32]:

replacer = RegexpReplacer()


# In[33]:

replacer.replace("can't is a contraction")#可以看见can't替换成cannot了


# In[34]:

replacer.replace("I should've done that thing I didn't do")


# In[35]:

#看出should've 和didn't被替换成了should have 和 did not


# In[36]:

##Accessing Corpora
#访问语料库


# In[37]:

from nltk.corpus import gutenberg


# In[41]:

for filename in gutenberg.fileids():

    r = gutenberg.raw(filename)

    w = gutenberg.words(filename)#词

    s = gutenberg.sents(filename)#句子

    v = set(w)

    print( filename, len(r)/len(w), len(w)/len(s), len(w)/len(v)) # 要按两次回车键才能显示结果。


# In[42]:

#打印出来的内容是：austen-emma.txt 4.609909212324673 24.822884416924666 24.63538599411087whitman-leaves.txt 4.591950052620365 36.44305882352941 10.809058552585665
#语料库的文件名    平均字长           平均句长          每个词平均出现的次数


# In[43]:

from nltk.book import *


# In[45]:

text1.concordance("monstrous")#找出包含monstrous的句子


# In[ ]:



