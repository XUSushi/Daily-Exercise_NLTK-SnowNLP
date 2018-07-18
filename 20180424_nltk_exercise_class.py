
# coding: utf-8

# In[1]:

from nltk.util import ngrams


# In[3]:

a="I love you babe, I love you forever".split(' ')


# In[4]:

b=ngrams(a,2)


# In[5]:

b


# In[6]:

for i in b:print(i)


# In[7]:

b1=ngrams(a,3)


# In[8]:

for i in b1:print(i)


# In[ ]:



