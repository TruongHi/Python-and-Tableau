# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:46:54 2022

@author: USER
"""
# Import pandas
import pandas as pd
# Import numpy
import numpy as np
# Import regex
import re
# import seaborn and matplotlib
import seaborn as sns 
import matplotlib.pyplot as plt

worldcup_players = pd.read_csv('C:/Users/USER/.spyder-py3/Project 3 Worldcups Report/WorldCupPlayers.csv')

worldcup = pd.read_csv('C:/Users/USER/.spyder-py3/Project 3 Worldcups Report/WorldCups.csv')

worldcup_matches = pd.read_csv('C:/Users/USER/.spyder-py3/Project 3 Worldcups Report/WorldCupMatches.csv')

# Clean worldcup data

# Convert all values to int or str
worldcup['Country'] = worldcup['Country'].astype('string')
worldcup['Winner'] = worldcup['Winner'].astype('string')
worldcup['Runners-Up'] = worldcup['Runners-Up'].astype('string')
worldcup['Third'] = worldcup['Third'].astype('string')
worldcup['Fourth'] = worldcup['Fourth'].astype('string')

# convert object to string, then remove (.) to convert to interger
worldcup['Attendance'] = worldcup['Attendance'].astype('string')
worldcup['Attendance'] = worldcup['Attendance'].str.replace(".", "", regex=False)
worldcup['Attendance'] = worldcup['Attendance'].astype(int) # OR worldcup['Attendance'] = pd.to_numeric(worldcup['Attendance'])

# Last but not least ! Check for duplicate values -> NONE 
worldcup[worldcup.duplicated()]

# Clean worldcup matches data

# Check for NAN values from world cup matches data set 
worldcup_matches.isna().sum()
# Remove NAN values from worldcup_matches data:
# worldcup_matches[~worldcup_matches['Year'].isna()] # rows which have valid entries, use ~
# worldcup_matches[worldcup_matches['Year'].isna()] # rows which have invalid entries
worldcup_matches[worldcup_matches['Year'].isna()] # 3720 rows × 20 columns

# Obtain only rows with valid Year values, drop all rows that contains NAN values
worldcup_matches.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True) # 850 rows × 20 columns after drop

# Not sure if these 2 columns are needed so better convert Year, MatchID from float to int that might be used later on
worldcup_matches['Year'] = worldcup_matches['Year'].astype(int)
worldcup_matches['MatchID'] = worldcup_matches['MatchID'].astype(int)

# Check for duplicate entries, if any, and drop them
worldcup_matches.duplicated().sum() # Count how many duplication are there in column -> 15 

# Detect duplicate values
check_duplicate_all = worldcup_matches[worldcup_matches.duplicated()]

# There are 15 duplicate entries - Let us drop them
worldcup_matches.drop_duplicates(inplace=True)

# Check if I drop duplicated correcly --> CORRECT !
check_duplicate_row = worldcup_matches[(worldcup_matches['Year'] == 2014) & (worldcup_matches['City'] == 'Belo Horizonte ') & (worldcup_matches['Away Team Name'] == 'Chile')] 

# Split the DateTime column into Date and Time
worldcup_matches = pd.concat([worldcup_matches[:], worldcup_matches['Datetime'].str.split('-', expand=True)], 
               axis=1).rename(columns={0: 'Date', 1: 'Time'}).drop(columns=['Datetime'])
# worldcup_matches[:] means all the rows and columns are selected
# worldcup_matches is as same as worldcup_matches

# Drop columns which are not needed
worldcup_matches.drop(columns=['Win conditions'], inplace=True) #drop columns

# Convert float interger
worldcup_matches['Attendance'] = worldcup_matches['Attendance'].astype(int)

# Convert initial values to interger for later analysis
worldcup_matches['Home Team Goals'] = worldcup_matches['Home Team Goals'].astype(int)
worldcup_matches['Away Team Goals'] = worldcup_matches['Away Team Goals'].astype(int)
worldcup_matches['RoundID'] = worldcup_matches['RoundID'].astype(int)

# Creat match_outcome column:
def match_outcome(df):
    if df['Home Team Goals'] > df['Away Team Goals']:
        return 'Home Team Win'
    if df['Home Team Goals'] < df['Away Team Goals']:
        return 'Away Team Win'
    else:
        return 'Draw'

worldcup_matches['Match Outcome'] = worldcup_matches.apply(match_outcome,axis=1)

# Strange country names :C�te d'Ivoire , rn">Serbia and Montenegro , 
# rn">Bosnia and Herzegovina , rn">United Arab Emirates , rn">Republic of Ireland , 
# rn">Trinidad and Tobago , rn">Bosnia and Herzegovina

List_wrong_name = list(worldcup_matches[worldcup_matches['Home Team Name'].str.contains('rn">')]['Home Team Name'])

correct_names = [i.split(">")[1] for i in List_wrong_name]

old_name = ['Germany FR', 'Maracan� - Est�dio Jornalista M�rio Filho', 'Estadio do Maracana',"C�te d'Ivoire"]
new_name = ['Germany', 'Maracan Stadium', 'Maracan Stadium',"Côte d'Ivoire"]

List_wrong_name = List_wrong_name + old_name
correct_names = correct_names + new_name

def correct_name(df):
    for index, string in enumerate(List_wrong_name):
        df = df.replace(List_wrong_name[index], correct_names[index])
    return df

worldcup_matches = worldcup_matches.apply(correct_name,axis=1)

worldcup = worldcup.apply(correct_name,axis=1)

worldcup_players = worldcup_players.apply(correct_name,axis=1)

# Clean worldcup_players data

worldcup_players.info()

# Check for NAN values from world cup players data set 
worldcup_players.isna().sum()
worldcup_players[worldcup_players['Position'].isna()]
worldcup_players[worldcup_players['Position'].isna()]
# fill NAN value columns with 0 
worldcup_players.fillna(0, inplace=True)

# Check for duplicate values 
worldcup_players.duplicated().sum()
worldcup_players[worldcup_players.duplicated()]

# There are 736 duplicate entries - Let us drop them
worldcup_players.drop_duplicates(inplace=True)

# Convert Event column to string type 
worldcup_players['Event'] = worldcup_players['Event'].astype('string')

# Exploratory Analysis and Visualization
# Top performant countries in World Cup
Winners = worldcup['Winner'].value_counts()
Runners_up = worldcup['Runners-Up'].value_counts()
Thirds = worldcup['Third'].value_counts()

performant_teams = pd.concat([Winners, Runners_up, Thirds], axis=1)
performant_teams.fillna(0, inplace=True)
performant_teams = performant_teams.reset_index()
performant_teams.fillna(0, inplace=True)
performant_teams = performant_teams.rename(columns={'index': 'Countries'})

# Number of Goals of top 10 Countries for all the world cups they've played
home_goals = worldcup_matches.groupby(['Year', 'Home Team Name'])['Home Team Goals'].sum()
away_goals = worldcup_matches.groupby(['Year', 'Away Team Name'])['Away Team Goals'].sum()

team_goals = pd.concat([home_goals, away_goals], axis=1)
team_goals.fillna(0, inplace=True)
team_goals['Goals'] = team_goals['Home Team Goals'] + team_goals['Away Team Goals']
team_goals = team_goals.reset_index()
team_goals.columns = ['Year', 'Country', 'Home Team Goals', 'Away Team Goals', 'Goals']
team_goals = team_goals.sort_values(by = ['Country', 'Year'], ascending = True)

goals = team_goals.groupby(['Country'])['Goals'].sum().sort_values(ascending=False).head(10)


a =  pd.merge([home_goals, away_goals], axis=1)


Total_lastest_covid_cases = Total_lastest_confirmed_cases.merge(Total_lastest_death_cases, how='inner', on='Country/Region')
Total_lastest_covid_cases = Total_lastest_covid_cases.merge(Total_lastest_recoveries, how='inner', on='Country/Region')
  






