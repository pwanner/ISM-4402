#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
all_data = pd.DataFrame()
df = pd.read_excel("datasets/data1.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("datasets/data2.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("datasets/data3.xlsx")
all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[2]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("datasets/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[6]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[8]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = 'SELECT * from test where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[10]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = "select name from sqlite_master where type = 'table';"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[12]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = 'SELECT * from scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




