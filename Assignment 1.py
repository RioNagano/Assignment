#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
bnbData = pd.read_csv("listings.csv")
print(bnbData.head(1))


# Find minimum or maximum of a value

# In[10]:


minValue = bnbData.min()
maxValue = bnbData.max()
print("Min Price : ", maxValue["price"])


# Eliminate null value

# In[14]:


newBnbDataDrop = bnbData.dropna()
print(newBnbDataDrop.isna().values.any())
print(len(newBnbDataDrop))


# Replace null value to certain value

# In[15]:


newBnbDataFill = bnbData.fillna("Value")
print(newBnbDataFill.isna().values.any())
print(len(newBnbDataFill))


# In[ ]:




