#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


df = pd.read_csv("C:/Users/JohanQ/Documents/UNA/Python/Semana8/Compras.csv",names=['producto','precio'])


# In[15]:


df['precio'].sum()


# In[16]:


df['precio'].mean()


# In[ ]:




