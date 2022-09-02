# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:11:57 2022

@author: Trường Hi 
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


data = pd.read_excel('C:/Users/USER/.spyder-py3/Project 6 Blog Sentiment Analysis/1.1 articles.xlsx')

data.describe()

data.info()

data['source_id'].value_counts()

data.groupby('source_id')['engagement_reaction_count'].sum()

data = data.drop('engagement_comment_plugin_count', axis=1)

def get_wife(name, surname, location):
    print('This is ' +name+' Her surname is ' + surname+' She is from ' +location)
    return name, surname, location

a = get_wife('Quyên', 'Đõ', 'Mai Thị Lưu')

def fav_food(food):
    for x in food:
        print('Top food is ' +x)
        

fastfood = ['burgers' , 'pizza', 'pie']

fav_food(fastfood)

# creating a keyword flag

keyword = 'crash'

#lets create a for loop to isolate title row

# length = len(data)
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0 
#     keyword_flag.append(flag)
    
# creating a function

def keywordflag(keyword):
    
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0 
        except:
            flag = 0 
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag('murder')
 
# creating a new column in dataframe

data['keyword_flag'] = pd.Series(keywordflag)

# Class type

class Car:
    type = 'Automobile' # class attribute
    def __init__(self,name,make,color):
        self.carname = name # instant attribute
        self.carmake = make
        self.carcolor = color
        
mycar = Car('glass' , 'mecerdes' , 'black')

# for attribute in a class

carname = mycar.carname
carmake = mycar.carmake
carcolor = mycar.carcolor

# SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# adding a for loop to extract sentimnet per title 

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)
for i in range(0,length):
    try:
        text = data['title'][i]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        post = 0
        neu = 0  
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment 
data['title_neu_sentiment'] = title_neu_sentiment 
    
data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=False)



