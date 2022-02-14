#!/usr/bin/env python
# coding: utf-8

# # Install the dependencies

# ### Open cmd in the directory project and run this comand:
# 

# In[ ]:


#pip install -r requirements.txt


# # Set up your libraries

# In[3]:


import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start_date = '2020-01-01'
end_date = '2022-02-14'


# # Chose your stocks

# In[4]:


AMZN = web.get_data_yahoo('AMZN', start_date, end_date)
AMZN = AMZN.groupby(pd.Grouper(freq='M')).mean()

AAPL = web.get_data_yahoo('AAPL', start_date, end_date)
AAPL = AAPL.groupby(pd.Grouper(freq='M')).mean()

GOOG = web.get_data_yahoo('GOOG', start_date, end_date)
GOOG = GOOG.groupby(pd.Grouper(freq='M')).mean()


# # Get the raw data

# In[5]:


AAPL.head()


# In[6]:


GOOG.head()


# In[7]:


AMZN.head()


# # Data visualization

# In[8]:


combined_series = pd.concat([AMZN['Adj Close'],
                            AAPL['Adj Close'],
                            GOOG['Adj Close']
                            ],axis = 1)

combined_series.columns = ["AMZN","AAPL","GOOG"]

combined_series.plot(grid=True, subplots= False, title="Closing prices from the pandemic")


# In[ ]:




