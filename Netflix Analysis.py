# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 04:22:39 2022

@author: USER
"""

# Import pandas
import pandas as pd
# Import numpy
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df_netflix_2019 = pd.read_csv('C:/Users/USER/.spyder-py3/Project 12 Netflix Analysis/netflix_titles.csv')

df_netflix_2019.info()

# Check duplocated. NONE
df_netflix_2019.duplicated().sum()

df_netflix_2019.shape

df_netflix_2019.isna().sum().sort_values(ascending=False) 

for column in df_netflix_2019.columns:
    percentage = df_netflix_2019[column].isnull().mean()
    print(f'{column}: {round(percentage*100, 2)}%')
    
mode = ''.join(df_netflix_2019['rating'].mode())
df_netflix_2019['rating'].fillna(mode, inplace=True)

df_netflix_2019['duration'].fillna(0, inplace=True)

#creating column (extract)
df_movie = df_netflix_2019[df_netflix_2019['type']=='Movie']
df_movie = df_movie.assign(minute = df_movie['duration'].str.extract(r'(\d+)', expand=False).astype(int))


minute = df_movie['duration'].str.extract(r'(\d+)', expand=False)
minute.info()

minute.fillna(0, inplace=True)       

# convert to interger type
minute = minute.astype(int)
                         
# convert Pandas DataFrame to a Series using squeeze: but not in this case, just example
minute = minute.squeeze()    

df_movie['minute'] = minute         
  
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.hist(df_movie['minute'])
fig.tight_layout()       
                  
df_movie.info()
df_movie['minute'].describe()          
                     
df_movie['rating'].value_counts()
wrong_values = df_movie['rating'].str.extract(r'(\d+\s(min))')
wrong_values = wrong_values[0]  
index_wrong_values = wrong_values[~wrong_values.isnull()].index
df_movie = df_movie.drop(index_wrong_values, axis=0)
 
df_movie_index = df_netflix_2019[df_netflix_2019['type']=='Movie'].index       
df_netflix_2019 = df_netflix_2019.drop(df_movie_index, axis=0)
df_netflix_2019['rating'].value_counts()  
 
df_netflix_2019_clean = pd.concat([df_netflix_2019, df_movie])


fig=df_netflix_2019['rating'].value_counts().plot.bar().get_figure()
fig.tight_layout()

df_netflix_2019.info()

df_movie['minute'].describe()
#outliers
df_movie[(df_movie['minute']<43) | (df_movie['minute']>158)]
#filtering outliers out
df_movie = df_movie[(df_movie['minute']>43) & (df_movie['minute']<158)]

# Final dataframe for later analysis
df_netflix_2019_clean = pd.concat([df_netflix_2019, df_movie])

df_netflix_2019_clean.to_csv('df_netflix_2019_clean.cvs')


