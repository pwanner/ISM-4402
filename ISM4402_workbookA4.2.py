#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import numpy as np
df['isFailing'] = np.where(df['grade']<70,
'yes', 'no')
df.tail(10)


# In[3]:


df['isFailingMale'] = np.where((df['grade']<70)
& (df['gender'] == 'male'),'yes', 'no')
df.tail(10)


# In[5]:


df['ExerciseStudy'] = np.where((df['exercise']>3)
& (df['hours']>17),'diligent', 'lazy')
df.tail(10)


# In[ ]:




