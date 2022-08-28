# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:32:00 2022

@author: Au Truong Hi
"""
## they’d like to see a report of borrowers who may have ##

### days.with.cr.line: The number of days the borrower has had a credit line.

### revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card
## billing cycle).

### revol.util: The borrower's revolving line utilization rate (the amount of the credit line used
## relative to total credit available).

### inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months. (If there
## are a lot of inquiries, that’s an issue)

### delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in
## the past 2 years.

### pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens,
## or judgments).

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

# method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)
    
loandata = pd.DataFrame(data)

# using EXP() to get the annual income
loandata['annualincome'] = np.exp(loandata['log.annual.inc'])

# using .apply() 
def check_fico(loandata):
    if loandata['fico'] >= 300 and loandata['fico'] < 400:
        return 'Very Poor'
    if loandata['fico'] >= 400 and loandata['fico'] < 600:
        return 'Poor'
    if loandata['fico'] >= 601 and loandata['fico'] < 660:
        return 'Fair'
    if loandata['fico'] >= 660 and loandata['fico'] < 780:
        return 'Good'
    if loandata['fico'] >=780:
        return 'Excellent'
    else:
        return 'Unknown'

loandata['fico.category'] = loandata.apply(check_fico, axis=1)
    

# lecture from Miss Stranger!
fruits = ['apple','peer','banana','cherry']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)
    
for x in range(0,4):
    y = fruits[x] + ' for sale'
    print(y)
    
length = len(fruits)    
for i in range(0,len(fruits)):
    print(i)
   
# for loop
length = len(loandata)
ficocategory = []   
for i in range(0,length):
    value = loandata['fico'][i]
    if value >= 300 and value < 400:
        category = 'Very Poor'
    elif value >= 400 and value < 600:
        category = 'Poor'
    elif value >= 601 and value < 660:
        category = 'Fair'
    elif value >= 660 and value < 780:
        category = 'Good'
    elif value >=780:
        category = 'Excellent'
    else:
        category = 'Unknown'
    ficocategory.append(category)
 
ficocat = pd.Series(ficocategory)

loandata['fico.category'] = ficocat

# while loop
length = len(loandata)
ficocategory = []   
i = 0
while i < len(loandata):
    value = loandata['fico'][i]
    if value >= 300 and value <= 400:
        category = 'Very Poor'
    elif value >= 400 and value <= 600:
        category = 'Poor'
    elif value >= 601 and value <= 660:
        category = 'Fair'
    elif value >= 661 and value <= 780:
        category = 'Good'
    elif value >=780:
        category = 'Excellent' 
    else:
        category = 'Unknown'
    ficocategory.append(category)
    i += 1
ficocat = pd.Series(ficocategory)
loandata['fico.category'] = ficocat


def interest_rate_type(loandata):
    if loandata['int.rate'] > 0.12:
        return 'High'
    if loandata['int.rate'] <= 0.12:
        return 'Low'

loandata['in.rate.type'] = loandata.apply(interest_rate_type, axis=1)

# Using .loc[]
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

loandata['purpose'].value_counts()
a = loandata.groupby(['purpose']).size()

a.plot.bar()
plt.show()

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='indianred')
plt.show()

loandata['dti'].describe()

loandata.to_csv('loan_cleaned.csv')

loandata['fico.category'].value_counts()




