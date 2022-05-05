#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for manipulations
import numpy as np
import pandas as pd

#for data visualizations
import matplotlib.pyplot as plt
import seaborn as sns

#for interactivity 
from ipywidgets import interact


# In[2]:


#lets read the datatset
data=pd.read_csv('data.csv')


# In[3]:


#lets check the shape of the dataset
print("shape of the dataset:",data.shape)


# In[4]:


data.head()


# In[5]:


#lets check if there is any missing value present in the dataset
data.isnull().sum()


# In[7]:


#lets check the crops present in this Dataset
data['label'].value_counts()


# In[8]:


print("Average Ratio of Nitrogen in the Soil: {0:.2f}".format(data['N'].mean()))
print("Average Ratio of Phosphorous in the Soil: {0:.2f}".format(data['P'].mean()))
print("Average Ratio of Potassium in the Soil: {0:.2f}".format(data['K'].mean()))
print("Average Ratio of Tempture in the Soil: {0:.2f}".format(data['temperature'].mean()))
print("Average Ratio of Humidity in the Soil: {0:.2f}".format(data['humidity'].mean()))
print("Average Ratio of PH in the Soil: {0:.2f}".format(data['ph'].mean()))
print("Average Ratio of Rainfall in the Soil: {0:.2f}".format(data['rainfall'].mean()))


# In[15]:


#lets check the Summary Statistics for each of the Crops 

@interact
def summary(crops = list(data['label'].value_counts().index)):
    x = data[data['label'] == crops]
    print("------------------------------------")
    print("Satistics for Nitrogon")
    print("Minimum Nitrigen required:",x['N'].min())
    print("avarage Nitrigen required:",x['N'].mean())
    print("Maxmum Nitrigen required:",x['N'].max())
    print("------------------------------------")
    print("Satistics for phoso")
    print("Minimum P required:",x['P'].min())
    print("avarage P required:",x['P'].mean())
    print("Maxmum P required:",x['P'].max())
    print("------------------------------------")
    print("Satistics for Po")
    print("Minimum Po required:",x['K'].min())
    print("avarage Po required:",x['K'].mean())
    print("Maxmum Po required:",x['K'].max())
    print("------------------------------------")
    print("Satistics for TEM")
    print("Minimum T required:",x['temperature'].min())
    print("avarage T required:",x['temperature'].mean())
    print("Maxmum T required:",x['temperature'].max())
    print("------------------------------------")
    print("Satistics for hu")
    print("Minimum hu required:",x['humidity'].min())
    print("avarage hu required:",x['humidity'].mean())
    print("Maxmum hu required:",x['humidity'].max())
    print("------------------------------------")
    print("Satistics for ph")
    print("Minimum ph required:",x['ph'].min())
    print("avarage ph required:",x['ph'].mean())
    print("Maxmum ph required:",x['ph'].max())
    print("------------------------------------")
    print("Satistics for rainfall")
    print("Minimum rainfall required:",x['rainfall'].min())
    print("avarage rainfall required:",x['rainfall'].mean())
    print("Maxmum rainfall required:",x['rainfall'].max())


# In[ ]:




