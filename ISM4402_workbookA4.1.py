#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[10]:


bins = [0,60,70,80,90,100]
group_names = ['F','D','C','B','A']


# In[11]:


df['lettergrade'] = pd.cut(df['grade'], bins,
labels=group_names)
df


# In[12]:


pd.value_counts(df['lettergrade'])


# In[19]:


bins01 = [0,80,100]
group_names01 = ['Fail','Pass']
df['passfail'] = pd.cut(df['grade'], bins01,
labels=group_names01)
df


# In[ ]:




