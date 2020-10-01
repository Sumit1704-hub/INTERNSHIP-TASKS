#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'darkgrid')


# In[3]:


course_information = pd.read_csv("/Users/sumittatawat/Downloads/INTERNSHIP/Project/courseraforums-master/data/course_information.csv")
course_posts = pd.read_csv("/Users/sumittatawat/Downloads/INTERNSHIP/Project/courseraforums-master/data/course_posts.csv")
course_threads = pd.read_csv("/Users/sumittatawat/Downloads/INTERNSHIP/Project/courseraforums-master/data/course_threads.csv")


# In[4]:


course_information.head(2)


# In[5]:


course_information.describe(), course_information.dtypes


# In[6]:


#checking for the missing values
course_information.isnull().sum()


# In[7]:


#creating a new dataset with values sorted in a descending order
course_info_sorted =course_information.copy()
course_info_sorted.sort_values(by='num_threads', ascending= False,inplace= True)


# # Figure 1

# In[8]:


plt.figure(figsize=(10,8))
sns.barplot(data = course_info_sorted, x ='course_id', y = 'num_threads', color='blue');
plt.xticks(rotation = 90, horizontalalignment = 'center');

plt.xlabel("Course Identity")
plt.ylabel("Number of threads")
plt.grid()
plt.tight_layout();
plt.title("Number of threads Vs. Course Identifiers")


# # Figure 3

# In[9]:


get_ipython().run_cell_magic('time', '', '#using gorupby to make another dataframe with user_type and post id\ncourse_posts_1 = course_posts.groupby(\'user_type\')[\'post_id\'].count()\n#converting it into a dataframe\ncourse_posts_1 = pd.DataFrame(data = course_posts_1)\n#resetting index\ncourse_posts_1.reset_index(inplace= True)\n#arranging the data into descending order and using inplace = True to make changes to the dataframe\ncourse_posts_1.sort_values(\'post_id\', ascending = False, inplace= True)\n\n#using seaborn to plot \nsns.barplot(data = course_posts_1, x = \'user_type\', y = \'post_id\', color = \'blue\')\nplt.yscale(\'log\');\nplt.xticks(rotation = 90, horizontalalignment = "center");\nplt.title("Total Number of Messages(log scale) by Coursera user type")\nplt.grid()')


# In[10]:


sns.distplot(course_posts['relative_t'])


# In[ ]:




