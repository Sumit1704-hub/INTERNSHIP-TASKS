#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[3]:


pip install matplotlib


# In[36]:


pip install seaborn as sns


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[2]:


df = pd.read_csv("/Users/sumittatawat/Downloads/INTERNSHIP/60k stackoverflow questions/data.csv")
df.shape


# In[3]:


df.head()


# In[4]:


df.dtypes


# In[5]:


df.Y.value_counts()


# In[6]:


df.dtypes


# - We can see that there are three categories and each one has 20,000 values
# - Using matplotlib to generate a bar chart

# In[7]:


#checking for the missing values
df.isnull().sum()


# In[8]:


sns.countplot(data = df, x = 'Y');


# In[9]:


get_ipython().run_line_magic('history', '')


# In[ ]:




