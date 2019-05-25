#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[5]:


x = np.array([0,1,2,3])


# In[ ]:





# In[6]:


x


# In[7]:


y = np.array([2,3,4,5])


# In[8]:


y


# In[11]:


x * x


# In[10]:


x * y


# In[12]:


x * y


# In[13]:


x.sum()


# In[15]:


x**x


# In[22]:


N=x.size


# N

# In[23]:


N


# In[27]:


A=(x*y).sum()


# In[28]:


A


# In[29]:


B=(x.sum())*(y.sum())


# In[30]:


B


# In[31]:


C=(x**2).sum()


# In[32]:


C


# In[33]:


D=(x.sum())**2


# In[34]:


D


# In[45]:


Ra=((N*A)-B)/((N*C)-D)


# In[46]:


Ra


# In[50]:


E=((x**2).sum())*(y.sum())


# In[51]:


E


# In[52]:


F=(x.sum())*((x*y).sum())


# In[53]:


F


# In[54]:


G=(x**2).sum()


# In[57]:


G


# In[58]:


H=(x.sum())**2


# In[59]:


H


# In[60]:


Rb=(E-F)/((N*G)-H)


# In[61]:


Rb


# In[62]:


import matplotlib.pyplot as plt


# In[63]:


plt.scatter(x,y)


# In[67]:


z = np.array([10,11,12])


# In[66]:


z + 2


# In[69]:


mi_recta=lambda w: w+2


# In[70]:


mi_recta(np.arange(10))


# In[72]:


plt.plot(np.arange(10,30),mi_recta(np.arange(10,30)))


# In[ ]:


plt.scatter(np.arange(10,30)mi_recta(np.arange(10,30)))
plt.plot(np.arange(10,30),mi_recta(np.arange(10,30)))
plt.show()

