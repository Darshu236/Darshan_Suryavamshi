#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats import chi2


# In[6]:


df = pd.read_csv("dist.csv")
df


# In[7]:


df.info()


# In[8]:


average_annual_rainfall = df.groupby('District')['Actual (mm)'].mean()
print(average_annual_rainfall)


# In[9]:


highest_rainfall_district = df.loc[df['Actual (mm)'].idxmax()]
lowest_rainfall_district = df.loc[df['Actual (mm)'].idxmin()]

print("District with highest rainfall:")
print(highest_rainfall_district[['District', 'Actual (mm)']])

print("\nDistrict with lowest rainfall:")
print(lowest_rainfall_district[['District', 'Actual (mm)']])


# In[15]:


average_annual_rainfall.plot(figsize = (20,5))


# In[80]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a DataFrame named 'data'

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(data['District'], data['Normal (mm)'], label='Normal Rainfall', marker='o')
plt.plot(data['District'], data['Actual (mm)'], label='Actual Rainfall', marker='x')
plt.title('Comparison of Normal and Actual Rainfall')
plt.xlabel('District')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[99]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(data['Actual (mm)'], bins=20, color='blue', alpha=0.7)
plt.title('Distribution of Actual Rainfall')
plt.xlabel('Actual Rainfall (mm)')
plt.ylabel('Frequency')
plt.show()


# In[18]:


import pandas as pd

df = pd.read_csv("dist.csv")

# Calculate the average annual rainfall for each district
average_annual_rainfall = df.groupby('District')['Actual (mm)'].mean()

# Create a pie chart
plt.figure(figsize=(8, 8))
average_annual_rainfall.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Average Annual Rainfall')
plt.show()


# In[19]:


pip install joypy


# In[25]:


# Create a heatmap
sns.set_theme()
sns.set(rc={'figure.figsize': (10, 8)})

heatmap = sns.heatmap(df[['District', 'Normal (mm)', 'Actual (mm)']].set_index('District'), annot=True, cmap='YlGnBu')
heatmap.set_title('Comparison of Normal and Actual Rainfall')
plt.show()


# In[28]:


average_annual_rainfall = df.groupby('District')['Actual (mm)'].mean()

# Create a bar chart
plt.figure(figsize=(12, 6))
average_annual_rainfall.plot(kind='bar')
plt.title('Average Annual Rainfall by District')
plt.xlabel('District')
plt.ylabel('Average Annual Rainfall (mm)')
plt.xticks(rotation=45, ha='right')
plt.show()





# In[29]:


# Create a box plot
plt.figure(figsize=(10, 6))
df.boxplot(column='Actual (mm)', by='District', rot=45)
plt.title('Annual Rainfall Distribution by District')
plt.xlabel('District')
plt.ylabel('Annual Rainfall (mm)')
plt.show()

