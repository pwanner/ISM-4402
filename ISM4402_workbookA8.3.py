#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
                          np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[7]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df


# In[11]:


plt.scatter(df['hours'], df['grade'])


# In[12]:


plt.scatter(df['grade'], df['hours'])


# In[ ]:




