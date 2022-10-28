#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[83]:


stock_data = pd.read_csv('HistoricalQuotes.csv')
stock_data


# In[84]:


#stock_data.dtypes
stock_data.columns


# In[85]:


stock_data.dtypes
#stock_data.info


# In[86]:


stock_data[' Volume']= stock_data[' Volume'].astype('int')
stock_data


# In[87]:


stock_data.columns= ['Date', 'Close/Last', 'Volume', 'Open', 'High', 'Low']
stock_data.columns


# In[88]:


stock_data['Close/Last'] = stock_data['Close/Last'].replace({'\$': ''}, regex=True)
stock_data['Open'] = stock_data['Open'].replace({'\$': ''}, regex=True)
stock_data['High'] = stock_data['High'].replace({'\$': ''}, regex=True)
stock_data['Low'] = stock_data['Low'].replace({'\$': ''}, regex=True)
stock_data["Date"] = pd.to_datetime(stock_data["Date"])
stock_data


# In[78]:


stock_data['High']=stock_data['High'].astype('float')
stock_data


# In[89]:


stock_data.dtypes


# In[80]:


stock_data.sort_values(by='High',ascending = False)


# In[90]:


stock_data.to_csv('stock_data_cleaned.csv')


# In[129]:


tweets = pd.read_csv('archive/Tweet.csv')
tweets.head()


# In[130]:


tweets.dtypes


# In[131]:





# In[ ]:





# In[132]:


tweets['post_date']=pd.to_datetime(tweets['post_date'],unit='s')
tweets['post_date'] = pd.to_datetime(tweets['post_date'].apply(lambda date: date.date()))


# In[133]:


tweets.tail()


# In[135]:


tweets.dtypes


# In[136]:


tweets.to_csv('Tweet.csv')


# In[ ]:




