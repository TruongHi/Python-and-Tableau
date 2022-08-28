# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:59:19 2022

@author: USER
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dhminh1024/practice_datasets/master/titanic.csv')

df.info()

# the survival rate (percentage of number of suvivals / total)
df[df['Survived'] == 0].shape[0] / df['Survived'].shape[0]
df['Survived'].mean()

# unique names of classes on the ship.
df['Pclass'].unique()

# Which class was the most crowded?
df['Pclass'].value_counts()

# unique names of the names of the habours where passengers embarked?
df['Embarked'].unique()

# which class’ ticket was the most expensive and how much was it?
df.groupby('Pclass')['Fare'].mean()

# bigger family paid less to get on the ship
df.groupby('FamilySize')['Fare'].mean()
          
# bigger family would have better chance to survive
df.groupby('FamilySize')['Survived'].mean()

# What happened to the members of the biggest family: Who are they? Did they all survive, partly survive, or all die?
Biggest_Family = df[df['FamilySize'] == 10]

# pivot function   
pd.pivot_table(df, 
                values=None, 
                index=None, 
                columns=None, 
                aggfunc='mean', 
                fill_value=None, 
                margins=False, 
                dropna=True, 
                margins_name='All', 
                observed=False, 
                sort=True)
    
# Within that most expensive class, where did its passengers embark and how many of them from each harbour?
df.groupby('Pclass')['Embarked'].value_counts()

df[df['Pclass'] == 1]['Embarked'].value_counts()

# the average ticket fare by both Pclass and harbour
df.groupby(['Pclass','Embarked'])['Fare'].mean()


def check_age(df):
    if df['Age'] <1:
        return 'Infants'
    if df['Age'] <10:
        return 'Children'
    if df['Age'] <18:
        return 'Teens'
    if df['Age'] <40:
        return 'Adults'
    if df['Age'] <60:
        return 'Middle Age'
    if df['Age'] >= 60:
        return 'Elders'
    
df['AgeRange'] = df.apply(check_age, axis=1)


a = pd.pivot_table(data=df,
               index='Pclass',
               columns=['AgeRange','Sex'],
               values='Survived',
               aggfunc='count')

Survived = df[df['Survived'] == 0]
Survived.groupby(['AgeRange','Sex'])['Survived'].value_counts()

def dead_alive(df):
    if df['Survived'] == 1:
        return 'Alive'
    if df['Survived'] == 0:
        return 'Dead'

df['Survival Status'] = df.apply(dead_alive, axis=1)

df['Name'].str.contains('Masabumi Hosono')

df['FamilySize'] = df['SibSp'] + df['Parch']

b = df[df['Ticket'] == '349909']
b = df[(df['FamilySize'] == 4) & (df['AgeRange'] == 'Children')]
c = df[(df['AgeRange'] == 'Children') & (df['Survival Status'] == 'Dead')]

Allision = df[df['Name'].str.contains("Allison")]

Thien_kim_tieu_thu = df[(df['AgeRange'] == 'Adults') & (df['Sex'] == 'female') & (df['Pclass'] == 1)]

df.info()
Ticket_3101295 = df[df['Ticket'] == '3101295']

df.groupby('AgeRange')['Survived'].mean()
df.groupby('Pclass')['Survived'].mean()


# Masabumi Hosono the Japanese man who survived
Panula_family = df[df['Name'].str.contains("Panula")]

df.to_csv('Titanic_clean.cvs')

unlucky_guys = df[df['Embarked'].isna()]