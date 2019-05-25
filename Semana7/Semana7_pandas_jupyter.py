#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


from pandas import Series, DataFrame


# In[4]:


obj = pd.Series([4,7,-5,3])


# In[5]:


obj


# In[6]:


obj.index


# In[9]:


obj2 = pd.Series([4,7,-5,3],index=['d','b','a','c'])
obj2
obj2.index


# In[10]:


obj2


# In[13]:


obj2['a']


# In[14]:


obj2[['a','b','c']]


# In[15]:


obj2[obj2 < 0]


# In[16]:


import numpy as np


# In[17]:


'z' in obj2


# In[18]:


'a' in obj2


# In[19]:


np.exp(obj2)


# In[20]:


sdata = {'Ohio': 3500,'Texas': 71000,'Oregon': 16000,'Utah': 5000}
obj3 = pd.Series(sdata)
obj3


# In[21]:


datos = {'Español': 90,'Mate': 80,'Sociales': 85,'Ciencias': 95}
Juan = pd.Series(datos)
Juan


# In[22]:


promedio = Juan.sum()/Juan.size


# In[23]:


promedio


# In[24]:


max = Juan.max()
max


# In[25]:


min = Juan.min()
min


# In[26]:


Juan[Juan < 90]


# In[27]:


notas = pd.Series(Juan, name='Notas de Juan')
notas


# In[28]:


notas.mean()


# In[29]:


notas.max()


# In[30]:


notas.min()


# In[31]:


notas[notas>=90]


# In[ ]:




