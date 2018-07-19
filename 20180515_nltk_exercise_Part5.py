
# coding: utf-8

# In[7]:

#外部文档操作

# 读取一个txt文件（在本地D盘建立了"good.txt"和"document.txt"文件）


# In[8]:

f = open('d:/document.txt')


# In[9]:

raw = f.read()


# In[10]:

##打印"good.txt"内容。# 即使打印Walden这样比较大的文件也比较快


# In[12]:

f = open ('d:/good.txt')


# In[14]:

f.read()


# In[15]:

f.close()


# In[16]:

# 建立自己的语料库，并对语料库里的文件进行检索

# 第一步


# In[6]:

corpus_root = 'D:/Python/my own data'


# In[7]:

from nltk.corpus import PlaintextCorpusReader


# In[8]:

wordlists = PlaintextCorpusReader(corpus_root, 'article1.txt')
#在这个目录下提前写好Walden.txt文件
#把Walden.txt文件里的内容处理到wordlists中


# In[9]:

wordlists.fileids()#该函数查看wordlists的范围


# In[10]:

wwordlists = PlaintextCorpusReader(corpus_root, '.*')
#注意这里的‘.*’具有贪婪性质，会最大限度地匹配，匹配到不能匹配为止，根据后面地正则表达式会回溯


# In[11]:

wwordlists.fileids()#可以看到把这个目录下地所有内容都匹配了


# In[30]:

# 第二步


# In[16]:

import nltk
from nltk.corpus import PlaintextCorpusReader


# In[24]:


n = nltk.word_tokenize(wordlists.raw(fileids="article1.txt"))#处理article2


# In[25]:

complete_Walden = nltk.Text(n)


# In[27]:

complete_Walden.concordance("people")#查找people这个词


# In[28]:

#获取网络文本


# In[30]:

#from urllib import urlopen
#这是python2的方法。
'''
python2和python3在导入urlrequest的方式都不一样。 
python2是这样：import urllib2 
而python3里面把urllib分开了，分成了urlrequest和urlerror，在这里我们只需导入urlrequest即可。from urllib.request import urlopen
'''


# In[31]:

from urllib.request import urlopen


# In[32]:

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"


# In[34]:

html = urlopen(url).read()
#读上面这个网址的内容，存在html中


# In[35]:

html[:60]


# In[36]:

# 接下来输入print html可以看到HTML 的全部内容，包括meta 元标签、图像标签、map 标签、JavaScript、表单和表格。


# In[37]:

print(html)


# In[38]:

## NLTK本来提供了一个辅助函数nltk.clean_html()将HTML 字符串作为参数，返回原始文本；但现在这个函数已经不被支持了，而是用BeautifulSoup的函数get_text()。


# In[ ]:




# In[40]:

from bs4 import BeautifulSoup


# In[41]:

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"


# In[43]:

html = urlopen(url).read()


# In[46]:

#BeautifulSoup就是Python的一个HTML或XML的解析库，
#我们可以用它来方便地从网页中提取数据
'''
BeautifulSoup可以处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。BeautifulSoup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。


'''


# In[47]:

soup = BeautifulSoup(html,"lxml")
#教材上是soup = BeautifulSoup(html)，但是运行时会报错，改为这样
#lxml HTML 解析器BeautifulSoup(markup, "lxml")速度快、文档容错能力强需要安装C语言库


# In[49]:

print (soup.get_text())
#获取文本
#获取文本可以用string属性，还有一个方法那就是get_text()，同样可以获取文本值。


# In[50]:

# 对网络文本分词


# In[51]:

from bs4 import BeautifulSoup


# In[52]:

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"


# In[54]:

html = urlopen(url).read()


# In[56]:

soup = BeautifulSoup(html,"lxml")


# In[59]:

raw = BeautifulSoup.get_text(soup)#获得网址中的文字


# In[58]:

from nltk.tokenize import word_tokenize#调用分词


# In[60]:

token = nltk.word_tokenize(raw)#把从网上抓到的文字分词


# In[61]:

print(token)


# In[62]:

# 重点


# In[63]:

s = [u'r118', u'BB']


# In[64]:

[str(item) for item in s]


