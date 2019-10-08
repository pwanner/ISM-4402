#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]


# In[2]:


GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
columns=['Names','Grades'])
df


# In[4]:


df['Grades'].count() # number of values


# In[5]:


df['Grades'].mean() # arithmetic average


# In[6]:


df['Grades'].std() # standard deviation


# In[7]:


df['Grades'].min() # minimum


# In[8]:


df['Grades'].max() # maximum


# In[9]:


df['Grades'].quantile(.25) # first quartile


# In[10]:


df['Grades'].quantile(.5) # second quartile


# In[11]:


df['Grades'].quantile(.75) # third quartile


# In[12]:


# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
df['Grades'].mean()
# finds the median of the values in a column
# median = the middle value if they are sorted in order
df['Grades'].median()
# finds the mode of the values in a column
# mode = the most common single value
df['Grades'].mode()


# In[13]:


# computes the variance of the values in a column
df['Grades'].var()


# In[14]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[15]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df1 = pd.DataFrame(data=GradeList,
columns=['Names','Grades','BS Degrees','MS Degrees','PHD Degrees'])
df1


# In[16]:


df1['BS Degrees'].count() # number of bs degree values


# In[17]:


df1['Grades'].mean() # arithmetic average


# In[18]:


df1['Grades'].std() # standard deviation


# In[19]:


df1['MS Degrees'].min() # minimum


# In[20]:


df1['PHD Degrees'].max() # maximum


# In[21]:


df1['Grades'].quantile(.25) # first quartile


# In[22]:


df1['Grades'].quantile(.5) # second quartile


# In[23]:


df1['Grades'].quantile(.75) # third quartile

