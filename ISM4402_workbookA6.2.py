#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit()
result.summary()


# In[3]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours',
data=df).fit()
result.summary()


# In[16]:


import numpy as np
df['genderInt'] = np.where(df['gender']=='male',0,1)
df.tail()


# In[17]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ genderInt + exercise + hours',
data=df).fit()
result.summary()


# In[ ]:




