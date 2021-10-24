#!/usr/bin/env python
# coding: utf-8

# # Machine Learning - Linear Regression in Python

# Notes on implementing Linear Regression in python.
# 
# 1. Data Analysis
# 2. Simple Linear Regression
# Gradient Descent Python Implementation
# Scipy Implementation
# Scikit-Learn Implementation
# Statsmodel Implementation
# Multi-step visual of Gradient Descent
# Animating the Gradient Descent
# 3. Multi Linear Regression
# Gradient Descent Python Implementation
# Scikit-Learn Implementation
# Solving with Normal Equation
# Scipy Implementation
# Statsmodel Implementation
# 
# https://github.com/tatwan/Linear-Regression-Implementation-in-Python/blob/master/Linear_Regression_Python.ipynb
#Importing needed libraries
# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dataset = pd.read_csv('E:\Ml_practice_code\Linear_regration\datasets/kc_house_data.csv')


# In[4]:


dataset


# In[5]:


X = dataset.drop(['price', 'id', 'date'],  axis=1)


# In[6]:


X


# In[7]:


Y = dataset[['price']]


# # 1. Data Analysis

# In[8]:


X.info()


# In[ ]:




