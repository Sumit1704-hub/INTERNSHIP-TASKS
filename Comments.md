# Task4

1. We will be using google colab to extract our features therefore we will first open a python notebook on google colab

2. We will start with importing the libraries that we will be using to extract features
```
import pandas as pd
import numpy as np 
from datetime import datetime
```

3. We will then import our dataset using pandas
```
course_information = pd.read_csv("/content/course_information.csv")
course_posts = pd.read_csv("/content/course_posts.csv")
course_threads = pd.read_csv("/content/course_threads.csv")
```

4. We will create a new column which will tell us if the parent_id is 0 or not:
```
#Generating a column where post_id = 0

course_posts['is_post'] = course_posts.parent_id==0
```
5. Once we have this new column we can now use it to get the count of posts and comments
  - We will first generate a new dataframe "tmp" where will will get the count of post_id using .groupby count() function
  -We will then create a new variable named count which will have the values of post_id and drop post_id from our dataset to avoid unnecessary iterations. Once we      do it we will then check the first 5 rows using head functions
```
#using groupby.count function to group the variables 

tmp = course_posts.groupby(['course_id', 'thread_id', 'is_post']).count()[['post_id']].reset_index()

# renaming the varibale 'post_id as count

tmp['count'] = tmp['post_id']
tmp.drop('post_id', axis=1, inplace=True)
tmp.head()
```

6. Now we will seperate the number of posts , first we create a new column named num_posts and assign it with the value 0. Then we use .loc function to check if the is_post condition is True, if yes we move the values of count to our newly generated column num_posts
```
#generating a new column with the name num_posts and assigning it value as 0

tmp['num_posts'] = 0

#checking if it's a post if yes replacing it with the value from count

tmp.loc[tmp.is_post == True, 'num_posts'] = tmp['count']
tmp.head()
```

7. Similarly we will get the number of comments:
```
#if the condition is false inserting values form count to num_comments

tmp['num_comments'] = 0

tmp.loc[tmp.is_post==False, 'num_comments'] = tmp['count']
tmp.head()
```

8. We will now use groupby.max() and reset the index
```
#using groupby.max and resetting the index

tmp = tmp.groupby(['course_id', 'thread_id']).max().reset_index()

tmp.head()

```
9. As per the research paper the number of messages is reffered as a combination of posts and comments
```
tmp['num_messages'] = tmp.num_posts + tmp.num_comments
tmp.head()
```

10. Extracting feature average response time:
  - first we need to convert the timsetamp provided to us which is in unix timestamp format, we will generate a function for that and map to the column we need to       change
  ```
  #Generating a function to convert unix timestamp to date and time

  def unix_to_time(o):
  return datetime.utcfromtimestamp(o).strftime('%Y-%m-%d %H:%M:%S')
  
  adding a new column with post_time but in datetime format for better analysis

  course_posts['post_time_t'] = course_posts.post_time.map(unix_to_time)

  ```

  - Getting the date and time for the last post by using groupby.max() function
  ```
  saving the time of last post by using groupby.max() function in a new dataset

  last_post = course_posts.groupby(['course_id','thread_id'])['post_time_t'].max().reset_index()

  #renaming the columns for better readability
  last_post.columns = ['course_id', 'thread_id', 'last_post']
  last_post.head()
  ```
  
  - We will repeat the same step but with groupby.min() function
  ```
  #performing similar actions from last cell but will use groupby.min() function to find the time of first post

   first_post = course_posts.groupby(['course_id','thread_id'])['post_time_t'].min().reset_index()
  first_post.columns = ['course_id', 'thread_id', 'first_post']
  first_post.head()
  ```
  
  - Now that we have our first and last post we will merge it into our data
  ```
  #merging our data 
  avg_resp_time = first_post.merge(last_post).merge(tmp)
  avg_resp_time.head()
  ```
  
  - We will again convert the datetime using .datetime function from pandas for better analysis
  ```
  # converting the datetime using pandas

  avg_resp_time['last_post'] = pd.to_datetime(avg_resp_time.last_post)
  avg_resp_time['first_post'] = pd.to_datetime(avg_resp_time.first_post)
  ```
  - Finally we have all the data to get the Average Response Time, we will now apply the formula as provided in the research paper:
  ```
  #getting the avergae response time as per the formula provided in the research paper

  avg_resp_time['avg_resp_time'] = (avg_resp_time.last_post-avg_resp_time.first_post)/avg_resp_time.num_messages
  avg_resp_time.head()
  ```
  
11. Extracting feature Message Rate:
  - We will first generate a function which will give us the 60 percent of the final messages
  ```
  #generating a function to get the 60% of it's final messages
  def perc_60(o):
  return np.percentile(o, 60)
  ```
  - using groupby funtion. to get course_if, thread_id with post_time then converting it into an array so that we can map our function from above cell to it
  ```
  avg_resp_time['msg_rate'] = course_posts.groupby(['course_id', 'thread_id'])['post_time'].apply(np.array).reset_index()['post_time'].map(perc_60)
  ```
  - changing the datetime format again
  ```
  avg_resp_time['msg_rate'] = avg_resp_time.msg_rate.map(unix_to_time)
  avg_resp_time.head()
  ```
12. Extracting Feature Day of the Week:
- Using .weekday() function to get the day of the week 
```
avg_resp_time['day_of_week'] = avg_resp_time.first_post.dt.weekday
```
13. Feature Relative time is already provided to us in course_posts dataset:
```
pd.DataFrame(course_posts.relative_t.head(5))
```
14. Results: All features have been successfully extracted from the dataset
