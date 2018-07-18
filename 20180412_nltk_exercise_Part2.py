
# coding: utf-8

# In[5]:

#将文本分出句子
para = "Hello World. It's good to see you. Thanks for buying this book."


# In[2]:

from nltk.tokenize import sent_tokenize


# In[3]:

sent_tokenize(para)#使用这个函数分成句子，根据.分的


# In[6]:

pp="你好，我来自中国，很高兴认识你！你来自哪里呢？哦。比利时。"


# In[7]:

sent_tokenize(pp)#可以看出识别中文的符号是非常无力的，完全无法根据中文分好


# In[8]:

ppp="Hello World.How are you? It's good to see you. Thanks for buying this book."


# In[9]:

sent_tokenize(ppp)#根据结果可以看出，是按照句号分的，？就不会给分出来


# In[10]:

#将句子分词


# In[11]:

from nltk.tokenize import word_tokenize


# In[14]:

word_tokenize('Hello World. How are you?')
#结果：['Hello', 'World', '.', 'How', 'are', 'you', '?']


# In[16]:

word_tokenize('Hello World.How are you?')
#结果：['Hello', 'World.How', 'are', 'you', '?']


# In[17]:

#对比上面两个语句可知是按照空格分的，'Hello World.How are you?'
#因为'World.How'没空格，被分在了一起


# In[18]:

#word_tokenize等同于


# In[19]:

from nltk.tokenize import TreebankWordTokenizer


# In[20]:

tokenizer = TreebankWordTokenizer()


# In[21]:

tokenizer.tokenize('Hello World. How are you?')


# In[26]:

#也等效于
import nltk


# In[23]:

text = "Hello. Isn't this fun?"


# In[24]:

pattern = r"\w+|[^\w\s]+" 
# r：regular expression；双引号""可以用单引号''代替；\w表示单词字符，等同于字符集合[a-zA-Z0-9_]；+表示一次或者多次，等同于{1,}，即c+ 和 c{1,} 是一个意思；"|"：二选一，正则表达式中的"或"； [...]：字符集（字符类），其对应的位置可以是字符集中任意字符，例如，a[bcd]表abe、ace和ade；^表示只匹配字符串的开头；\s匹配单个空格，等同于[\f\n\r\t\v]。


# In[28]:

nltk.tokenize.regexp_tokenize(text, pattern) 


# In[1]:

#使用正则表达式切分句子


# In[2]:

from nltk.tokenize import RegexpTokenizer 
#RegexpTokenizer：正则表达式分词器，使用正则表达式对文本进行处理，就不多作介绍。

tokenizer = RegexpTokenizer("[\w']+")
tokenizer.tokenize("Can't is a contraction.")


# In[3]:

tokenizer.tokenize("Aren't you crazy?")


# In[4]:

from nltk.tokenize import regexp_tokenize#我们需要借助正则表达式的强大能力来完成分词任务
regexp_tokenize("Can't is a contraction.", "[\w']+")


# In[5]:

#训练句子分词器


# In[6]:

from nltk.tokenize import PunktSentenceTokenizer


# In[7]:

from nltk.corpus import webtext


# In[8]:

text = webtext.raw('overheard.txt')


# In[9]:

sent_tokenizer = PunktSentenceTokenizer(text)#文本首先使用 PunktSentenceTokenizer 分割成句子。


# In[10]:

#将这个结果和默认分句器比较


# In[11]:

sents1 = sent_tokenizer.tokenize(text)


# In[12]:

sents1[0]
#第一句


# In[13]:

from nltk.tokenize import sent_tokenize


# In[14]:

sents2 = sent_tokenize(text)


# In[15]:

sents2[0]


# In[16]:

sents1[678]#结果显示自己训练的好


# In[17]:

sents2[678]


# In[18]:

#筛选分好的句子里的停用词


# In[19]:

from nltk.corpus import stopwords

english_stops = set(stopwords.words('english'))
##英文停止词，set()集合函数消除重复项,english是有设定的一堆词的

words = ["Can't", 'is', 'a', 'contraction']

[word for word in words if word not in english_stops]


# In[20]:

#在词网上找一个词的同义词集


# In[21]:

#方法一


# In[22]:

from nltk.corpus import wordnet

syn = wordnet.synsets('cookbook')[0]

syn.name()


# In[23]:

syn.definition()


# In[24]:

#方法二


# In[25]:

from nltk.corpus import wordnet
syn = wordnet.synsets('motorcar')[0]
syn.name


# In[26]:

from nltk.corpus import wordnet as wn
wn.synsets("motorcar") # 括号内可以是单引号


# In[28]:

# WordNet层次结构（词汇关系） 上级概念与从属概念的关系


from nltk.corpus import wordnet as wn


# In[29]:

motorcar = wn.synset('car.n.01')


# In[30]:

types_of_motorcar = motorcar.hyponyms() 
#上级概念与从属概念的关系
#等号两边的表达式不能换位，否则会出现警示：can't assign to function call.


# In[31]:

types_of_motorcar


# In[32]:

# 部分整体关系（components (meronyms) holonyms）

from nltk.corpus import wordnet as wn

wn.synset('tree.n.01').part_meronyms()


# In[33]:

# 反义词关系
wn.lemma('beautiful.a.01.beautiful').antonyms()


# In[34]:

# 查看词汇关系和同义词集上定义的其它方法

dir(wn.synset('beautiful.a.01'))


# In[35]:

# Part-of-Speech (POS)

from nltk.corpus import wordnet

syn = wordnet.synsets('motorcar')[0]

syn.pos()#其中pos包括noun、verb、adj和adv，分别对应名词、动词、形容词和副词。


# In[ ]:



