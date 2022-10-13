# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:45:48 2022

@author: USER
"""


import pandas as pd
import numpy as np

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from itertools import product
import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt


import seaborn as sns
sns.set_style("whitegrid")

data = pd.read_csv('C:/Users/USER/.spyder-py3/Project 10 Siêu xe/toyota.csv')

'''The marketing team would like you to answer the following questions to help:
    
● Are there differences in the fuel types between best and least selling used cars?

● Are there common features among the least selling used cars?'''

data.info()

data.duplicated().sum()

data.drop_duplicates(inplace=True)

Car_models = list(data['model'].value_counts().index)

cars_2020 = data[data['year'] == 2020]

cars_2020['model'].value_counts()

data['transmission'].value_counts()

data['fuelType'].value_counts()

Electric_car = data[data['fuelType'] == 'Other']

data['fuelType'] = data['fuelType'].replace({'Other':'Electric'})

data['fuelType'].value_counts()

data['engineSize'].value_counts()

data['mpg'].describe()

data[data['mpg'] == 235]

data.groupby('year')['tax'].value_counts()

data.to_csv('Discount Motors.cvs')
    
data['year'].max()
    
Eletric_car = data[data['fuelType'] == 'Electric']

Eletric_car['mileage'].describe()

Eletric_car['engineSize'].value_counts()

