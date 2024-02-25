#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[24]:


data=pd.read_csv(r"C:\Users\souri\AppData\Local\Temp\adef43ce-2a63-455d-b609-49a4f16034b9_archive.zip.4b9\country_wise_latest.csv")


# In[25]:


data.head


# In[26]:


data.columns


# In[5]:


data.tail()


# In[6]:


data.describe()


# In[33]:


data.columns


# # relating the variables with scatterplots

# In[37]:


sns.relplot(x="Active",y="Confirmed",hue='New cases',data=data)


# In[40]:


data.columns


# In[41]:


sns.catplot(x="Active",y="Confirmed",data=data)


# In[ ]:




