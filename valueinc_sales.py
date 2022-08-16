# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:51:22 2022

@author: USER
"""
import pandas as pd
# file_name = pd.read_csv('file.csv')

data = pd.read_csv('C:/Users/USER/.spyder-py3/Project 1 Sales Analysis for Value Inc/transaction.csv', sep=';')

# Variable = dataframe['column_name']

data['CostPerTransaction'] = data['NumberOfItemsPurchased'] * data['CostPerItem']

data['ProfitPerItem'] = data['SellingPricePerItem'] - data['CostPerItem']

data['ProfitPerTransaction'] = data['NumberOfItemsPurchased'] * data['ProfitPerItem']

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']    

data['Markup'] = round(data['Markup'], 2)

data['Day'] = data['Day'].astype('string')

data['Year'] = data['Year'].astype('string')

data['Date'] = data['Day']+'-'+data['Month']+'-'+data['Year']+'-'+data['Time']

data['Date'] = pd.to_datetime(data['Date'])

data = pd.concat([data[:], data['ClientKeywords'].str.split(',', expand=True)], 
                 axis=1).rename(columns={0: 'ClientAge', 1: 'Clienttype',2:'LengthofContract'}).drop(columns=['ClientKeywords'])

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

seasons = pd.read_csv('C:/Users/USER/Desktop/DATAAnalyst/Spyder/value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = 'Month')

data.drop(columns=['Day','Month','Year','Time'], inplace=True) 

data.to_csv('ValueInc_Cleaned.cvs')

