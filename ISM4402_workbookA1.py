#!/usr/bin/env python
# coding: utf-8

# In[1]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[2]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[3]:


df.head()


# In[4]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[5]:


df.head()


# In[6]:


import pandas as pd
Location = "datasets/smallgrades.csv"
# To add headers as we load the data...
df = pd.read_csv(Location, names=['Names','Grades'])
# To add headers to a dataframe
df.columns = ['Names','Grades']


# In[7]:


df.head()


# In[8]:


import pandas as pd
Location = "all_040_in_08.P1.csv"
censusdf = pd.read_csv(Location)


# In[9]:


censusdf.head()


# In[10]:


import pandas as pd
Location = "all_040_in_08.P1.csv"
censusdf = pd.read_csv(Location)


# In[11]:


censusdf.head()


# In[14]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)


# In[15]:


df.head()


# In[20]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns=column)
df


# In[21]:


import pandas as pd
Location = "datasets/gradedata.xlsx"
df = pd.read_excel(Location)


# In[22]:


df.head()


# In[23]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[24]:


path_to_zip_file = "EDU.zip"
directory_to_extract_to = ""
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[ ]:




