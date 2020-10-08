# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q67L8HvaZ6GLS8ttLT5z7vXTSGe_THu-
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'darkgrid')

course_information = pd.read_csv("/content/course_information.csv")
course_posts = pd.read_csv("/content/course_posts.csv")
course_threads = pd.read_csv("/content/course_threads.csv")

course_information.head(2)

course_information.describe(), course_information.dtypes

#checking for the missing values
course_information.isnull().sum()

#creating a new dataset with values sorted in a descending order
course_info_sorted =course_information.copy()
course_info_sorted.sort_values(by='num_threads', ascending= False,inplace= True)

"""# Figure 1"""

plt.figure(figsize=(10,8))
sns.barplot(data = course_info_sorted, x ='course_id', y = 'num_threads', color='blue');
plt.xticks(rotation = 90, horizontalalignment = 'center');

plt.xlabel("Course Identity")
plt.ylabel("Number of threads")
plt.grid()
plt.tight_layout();
plt.title("Number of threads Vs. Course Identifiers")

"""# Figure 3"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# #using gorupby to make another dataframe with user_type and post id
# course_posts_1 = course_posts.groupby('user_type')['post_id'].count()
# #converting it into a dataframe
# course_posts_1 = pd.DataFrame(data = course_posts_1)
# #resetting index
# course_posts_1.reset_index(inplace= True)
# #arranging the data into descending order and using inplace = True to make changes to the dataframe
# course_posts_1.sort_values('post_id', ascending = False, inplace= True)
# 
# #using seaborn to plot 
# sns.barplot(data = course_posts_1, x = 'user_type', y = 'post_id', color = 'blue')
# plt.yscale('log');
# plt.xticks(rotation = 90, horizontalalignment = "center");
# plt.title("Total Number of Messages(log scale) by Coursera user type")
# plt.grid()

sns.distplot(course_posts['relative_t'])

course_information.head()

"""# Figure 2"""

# Figure 2(b)(the graph i made shows increasing trend where as the one in the paper shows a decreasing trend)
# for part a i cannot understand the variable used to represent thread size
f, ax = plt.subplots(figsize = (7,7) )
ax.set(xscale = "log", yscale = "log")
sns.scatterplot(x = course_information.num_threads, y = course_information.num_users)
plt.xlabel('Number of threads')
plt.ylabel('Number of Users')
plt.title('Log-Log plot of Count of Users Vs Number of messages');

"""Checking for the common variables in course threads and course posts"""

Threads_intersection_posts = course_threads.columns.intersection(course_posts.columns)
print(Threads_intersection_posts)

"""Merging two dataframes course threads and course posts"""

c = pd.merge(course_threads, course_posts, on = ("thread_id","course_id","forum_id" ))

c[:2]

"""Checking for the common variables in the merged file and the course information"""

info_threads_posts_intesection = c.columns.intersection(course_information.columns)
info_threads_posts_intesection

"""Merging all 3 dataframes together"""

all = pd.merge(c, course_information, on = "course_id")
all[:2]

all.columns

f, ax = plt.subplots(figsize = (7,7) )

sns.scatterplot(x = all.thread_id, y = all.post_id, hue = all.forum_id.where(all.forum_id == 3))

