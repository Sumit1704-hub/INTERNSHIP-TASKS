# INTERNSHIP-TASKS

1. We will be using colab for this task therefore we will open a google colab python notebook.

2. We will Download the Mooc dataset file using the link provided in Trello

3. Now that we have a new python notebook on colab we will start with importing libraries:
```
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'darkgrid')
```

2. We first need to upload our files to colab, then we will Read the dataset using pandas:
```
course_information = pd.read_csv("/content/course_information.csv")
course_posts = pd.read_csv("/content/course_posts.csv")
course_threads = pd.read_csv("/content/course_threads.csv")
```

3. Once we have successfully loaded our dataset we will then use it to do the further analysis:
```
course_information.shape, course_posts.shape, course_threads.shape
```
checking the shape of each csv file, this will give us the number of rows and columns of our dataset

4. For Figure 1, we will first create a new dataset where the number of threads are in descending order:
```
course_info_sorted =course_information.copy()
course_info_sorted.sort_values(by='num_threads', ascending= False,inplace= True)
```

5. Generating bar plot between course identifiers and number of threads usinig seaborn.
```
plt.figure(figsize=(10,8))
sns.barplot(data = course_info_sorted, x ='course_id', y = 'num_threads', color='blue');
plt.xticks(rotation = 90, horizontalalignment = 'center');

plt.xlabel("Course Identity")
plt.ylabel("Number of threads")
plt.grid()
plt.tight_layout();
plt.title("Number of threads Vs. Course Identifiers")
```

6. Observations for Figure 1:Number of threads Vs. Course Identifiers
- We can see that the least number of threads are associated with course named 'friendsmoneybytes' also the highest number of threads were associated with course "intropsych-001"
- The number of thread ranges from 103 to 9,300 with a mean of 1660 and a median of 904.5.

7. Moving to Figure 3:Total Number of Messages(log scale) by Coursera user type
- We used a group by function to get the count of the post_id to get the number of messages and then used it to plot a barplot between user type and number of messages(log scaled).
- We will also arrange our dataset in descending order with respect to post_id count.
- We will then use seaborn to generate a barplot between coursera user type and log scaled number of messages, the following commands will help us generate a neat plot with assigned labels and titles:
```
%%time
#using gorupby to make another dataframe with user_type and post id
course_posts_1 = course_posts.groupby('user_type')['post_id'].count().reset_index()

#arranging the data into descending order and using inplace = True to make changes to the dataframe
course_posts_1.sort_values('post_id', ascending = False, inplace= True)

#using seaborn to plot 
sns.barplot(data = course_posts_1, x = 'user_type', y = 'post_id', color = 'blue')
#adding titles to x and y axis
plt.xlabel("Coursera User Type")
plt.ylabel("Number of Messages")

#adding log scale to numnber of messages
plt.yscale('log');
plt.xticks(rotation = 90, horizontalalignment = "center");
plt.title("Total Number of Messages(log scale) by Coursera user type")
plt.grid()
```
Observations:
- Number of messages is highest for students and the lowest from coursera staff

8. As mentioned in the research paper and the dataset description we need to get a count of number of posts and number of comments. In the dataset desription for course_posts.csv, variable parent_id will help us seperate the number of comments and posts. 
- parent_id is categorical variable which represents:
    0 = posts
    Non-zero = comments

9. We will create a new column which will tell us if the parent_id is 0 or not:
```
course_posts['is_post'] = course_posts.parent_id==0
```

10. Once we have this new column we can now use it to get the count of posts and comments
- We will first generate a new dataframe "tmp" where will will get the count of post_id using .groupby count() function
```
tmp = course_posts.groupby(['course_id', 'thread_id', 'is_post']).count()[['post_id']].reset_index()
```

11. We will then create a new variable named count which will have the values of post_id and drop post_id from our dataset to avoid unnecessary iterations.
Once we do it we will then check the first 5 rows using head functions
```
tmp['count'] = tmp['post_id']
tmp.drop('post_id', axis=1, inplace=True)
tmp.head()
```

12. Now we will seperate the number of posts , first we create a new column named num_posts and assign it with the value 0. Then we use .loc function to check if the is_post condition is True, if yes we move the values of count to our newly generated column num_posts

```
#generating a new column with the name num_posts and assigning it value as 0

tmp['num_posts'] = 0

#checking if it's a post if yes replacing it with the value from count

tmp.loc[tmp.is_post == True, 'num_posts'] = tmp['count']
tmp.head()
```

13. Similarly we will get the number of comments:
```
#if the condition is false inserting values form count to num_comments

tmp['num_comments'] = 0

tmp.loc[tmp.is_post==False, 'num_comments'] = tmp['count']
tmp.head()
```

14. We will now use groupby.max() and reset the index
```
tmp = tmp.groupby(['course_id', 'thread_id']).max().reset_index()

tmp.head()
```

15. Now that we have the number of posts and comments, we will need our data from forum_id with category 3(Assignments) and 4(Study Groups/ Meetups) to generate the scatter plot
```
#creating a new dataset with values with forum id 4 and 3 and mering it with tmp dataset on course_id and thread_id

fig4_dat = course_threads.query("forum_id == 4|forum_id==3").merge(tmp, on=['course_id', 'thread_id'])
fig4_dat.head(2)
```
16. Once we have our data we will now remove unwanted variabled for our plot
```
fig4_dat = fig4_dat[['forum_id', 'num_posts', 'num_comments']]
fig4_dat.head(2)
```

17. We will now generate scatterplot with hue as forum_id
```
sns.scatterplot(data=fig4_dat, x='num_posts', y='num_comments', hue='forum_id')

#setting limits for x and y axis

plt.xlim(0,100)
plt.ylim(0,100)

#setting labels and the title
plt.xlabel("Number of Posts")
plt.ylabel("Number of Comments")
plt.title("Scatter plot showing relationship between Number of comments and number of posts for Assignments and Study Group");

```
Observations:
- the numbmer of comments for assignments is greater for  in the beginning and reduces with increasing posts(number of comments for initial posts is higher)
- the number of comments for Study group stays more or less similar throughout the plot

18. For Figure 2 I am unable to replicate the graph as the one I made shows increasing trend unlike the one mentioned in the research paper

19. For 5 and 6 as mentioned the data is not provided

20. Analysis:
- Insights on different usages of posts, comments and messages are provided using graphs
- Subforum participation evolves over normalized the course duration



