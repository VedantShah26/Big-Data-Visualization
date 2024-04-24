#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

df = pd.read_csv('/Users/shahv/OneDrive/Desktop/health/CVD_cleaned.csv')

df_subset = df.head(100000)

columns_to_select =  ['General_Health', 'Heart_Disease', 'Sex', 'Age_Category', 'Smoking_History', 'Alcohol_Consumption', 'Fruit_Consumption', 'Green_Vegetables_Consumption', 'FriedPotato_Consumption']
df_subset = df_subset[columns_to_select]

print("Number of rows in the dataset: ", len(df))

print("Subset of the dataset: \n", df_subset)

print(df_subset.isnull().sum())


# In[11]:


import csv
import redis
import json

r = redis.Redis(
        host='redis-15265.c245.us-east-1-3.ec2.redns.redis-cloud.com',
        port=15265,
        password='vVXz2jk1Iypby98KOeFnGCoB9u88g0Br',
        db=0,
        encoding='utf-8'
)

selected_rows = []
with open('/Users/shahv/OneDrive/Desktop/health/CVD_cleaned.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)
    for i, row in enumerate(csv_reader):
        if i >= 100000:
            break
        selected_row = {
            'General_Health': str(row[0]),  
            'Heart_Disease': str(row[3]),    
            'Sex': str(row[9]),              
            'Age_Category': str(row[10]),    
            'Smoking_History': str(row[14]), 
            'Alcohol_Consumption': float(row[15]),  
            'Fruit_Consumption': float(row[16]),    
            'Green_Vegetables_Consumption': float(row[17]), 
            'FriedPotato_Consumption': float(row[18])
        }
        selected_rows.append(selected_row)

for i, row in enumerate(selected_rows):
    r.set(f'data:{i}', json.dumps(row))

data_for_visualization = []
for i in range(100000):
    row_data = json.loads(r.get(f'data:{i}'))
    data_for_visualization.append(row_data)


# In[ ]:




