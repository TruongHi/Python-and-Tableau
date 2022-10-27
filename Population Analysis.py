# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:12:39 2022

@author: Trường Hi
"""

import pandas as pd

df_population = pd.read_csv('C:/Users/USER/.spyder-py3/Project 15 Population Analysis/population_total.csv')

df_population.info()

df_population.duplicated().sum()

df_population = df_population.drop_duplicates()

df_population = df_population.dropna()

df_population['country'].value_counts()

df_population['country'].str.contains('Viet').any()

Vietnam = df_population[df_population['country'].str.contains('Viet')]
              
Cambodia = df_population[df_population['country'].str.contains('Cambodia')]

Thailand = df_population[df_population['country'].str.contains('Thailand')]

Laos = df_population[df_population['country'].str.contains('Laos')]

Hong_Kong = df_population[df_population['country'].str.contains('Hong')]   

df_population = df_population.pivot(index='year', columns='country',
                                    values='population')         

df_population_analysis = df_population[['Vietnam', 'Cambodia', 'Laos', 
                               'Thailand', 'Hong Kong']]

df_population_analysis = pd.concat([Vietnam, Cambodia, Laos, Hong_Kong, Thailand])


df_population_analysis.to_csv('Population Analysis.cvs')

df_population_sample = df_population[df_population.index.isin([1980, 1990, 2000, 2010, 2020])]

df_population_sample.to_csv('population_sample.cvs')

df_population_analysis['year'] = pd.to_datetime(df_population_analysis['year'])

df_population_analysis.info()