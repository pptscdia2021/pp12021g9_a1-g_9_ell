#!/usr/bin/env python
# coding: utf-8

# In[7]:


# importamos las librerias necesarias
import pandas as pd


# In[8]:


df=pd.read_csv('acciones_bma.csv')


# In[20]:


df_min=df.sort_values(by=['Var.']).head(2)
df_min


# In[21]:


df_max=df.sort_values(by=['Var.']).tail(2)
df_max


# In[ ]:




