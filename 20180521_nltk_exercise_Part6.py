
# coding: utf-8
# In[65]:

#Default tagging
#默认标签


# In[66]:

#版本一
import nltk


# In[67]:

text=nltk.word_tokenize("We are going out.Come with me.")


# In[69]:

nltk.pos_tag(text)#pos_tag()函数可以获得标签


# In[70]:

# 版本二


# In[72]:

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)#把句子分成词

tokens


# In[73]:

tagged = nltk.pos_tag(tokens)


# In[74]:

tagged#打好标签了
'''
结果：
[('At', 'IN'),
 ('eight', 'CD'),
 ("o'clock", 'NN'),
 ('on', 'IN'),
 ('Thursday', 'NNP'),
 ('morning', 'NN'),
 ('Arthur', 'NNP'),
 ('did', 'VBD'),
 ("n't", 'RB'),
 ('feel', 'VB'),
 ('very', 'RB'),
 ('good', 'JJ'),
 ('.', '.')]
'''


# In[75]:

tagged[0:6]#打印前6个


# In[76]:

#Chunking and chinking with regular expressions
#用正则表达式分块


# In[77]:

# Chunking & Parsing

# Chart Parsing 是描述CFG(Context Free Grammar)语法的一种方法，两者不是平行关系。


# In[78]:

import nltk

 

grammar = r"""

NP: {<DT|PP\$>?<JJ>*<NN>} # chunk determiner/possessive, adjectives and nouns

{<NNP>+} # chunk sequences of proper nouns

"""


# In[79]:

cp = nltk.RegexpParser(grammar)


# In[81]:

tagged_tokens = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("golden", "JJ"), ("hair", "NN")] 
# 实际运用中，需先对"Rapunzel let down her golden hair."这句进行tokenization.


# In[82]:

print (cp.parse(tagged_tokens))#


# In[83]:

# CFG Parsing


# In[91]:

import nltk

# 这两行代码也可以写成：from nltk import CFG; groucho_grammar = CFG.fromstring("""

groucho_grammar = nltk.CFG.fromstring("""

S -> NP VP

PP -> P NP

NP -> D N | D N PP | 'I'

VP -> V NP | V PP

D -> 'an' | 'a' | 'my' | 'the'

N -> 'elephant' | 'pajamas'

V -> 'shot'

P -> 'in'

""")


# In[92]:

sent = "I shot an elephant in my pajamas".split() 
# 就分好词了，即：sent = ['I','shot','an','elephant','in','my','pajamas']


# In[93]:

sent


# In[94]:

parser = nltk.ChartParser(groucho_grammar) # Chart Parsing 是描述CFG语法的一种方法。


# In[95]:

all_the_parses = parser.parse(sent)#处理到all_the_parses中


# In[99]:

all_the_parses
type(all_the_parses)#查看这个的类型，是个生成器


# In[100]:

for parse in all_the_parses:

    print(parse)


# In[101]:

#遍历打印出来查看





