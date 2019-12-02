#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
Location = "datasets/axisdata.csv" 
df = pd.read_csv(Location)


# In[9]:


df.head()


# In[10]:


df.info()


# In[11]:


#Number 1
df["Cars Sold"].mean()


# In[12]:


#Number 2
df["Cars Sold"].max()


# In[13]:


#Number 3
df["Cars Sold"].min()


# In[16]:


#Number 4
df.groupby('Gender')['Cars Sold'].mean()


# In[23]:


#Number 5
df[(df['Cars Sold'] > 3)]['Hours Worked'].mean()


# In[22]:


#Number 6
df["Years Experience"].mean()


# In[24]:


#Number 7
df[(df['Cars Sold'] > 3)]['Years Experience'].mean()


# In[28]:


#Number 8
df.sort_values(['Cars Sold','SalesTraining'],ascending=[False, False])


# In[50]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.boxplot(by='Cars Sold',column='Hours Worked')


# In[109]:


df[(df['Cars Sold']==7) & (df['Hours Worked']==35)]


# In[110]:


df.hist(column='Cars Sold',by='SalesTraining')


# In[115]:


sums = df['Cars Sold'].groupby(df['Years Experience']).sum()
plt.pie(sums, labels=sums.index,autopct='%1.1f%%')
plt.axis('equal')
plt.show()


# In[116]:


sums = df['Cars Sold'].groupby(df['SalesTraining']).sum()
plt.pie(sums, labels=sums.index,autopct='%1.1f%%')
plt.axis('equal')
plt.show()


# In[ ]:




