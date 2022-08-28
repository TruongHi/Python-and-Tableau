# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:26:07 2022

@author: USER
"""
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recoveries = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

identifiers = confirmed.columns[:4]
values = confirmed.columns[4:]

confirmed_clean = confirmed.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

deaths_clean = deaths.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

recoveries_clean = recoveries.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

# Convert to proper date and time
confirmed_clean['Date'] = pd.to_datetime(confirmed_clean['Date'])
deaths_clean['Date'] = pd.to_datetime(deaths_clean['Date'])
recoveries_clean['Date'] = pd.to_datetime(recoveries_clean['Date'])

# Covid Cases Report on 4/22/2022
Covid_22_4_2022 = confirmed_clean[confirmed_clean['Date'] == '4/22/22']

# Lastest Covid Cases 
latest_covid_date = confirmed_clean['Date'].values[-1] # --> Lastest update on 8/5/2022
latest_cases = confirmed_clean[confirmed_clean['Date'] == confirmed_clean['Date'].values[-1]]

-------------------------------------------------------------------------------------------------------------------------------------------------------

def latest_situation(classified_identities):
    return classified_identities[classified_identities['Date'] == confirmed_clean['Date'].values[-1]].groupby('Country/Region')['Cases'].sum().reset_index

latest_situation(confirmed_clean)

# Write a function that reports the latest situation of the Corona Virus in a given country. 
# The function takes one argument as input - the country where the report is from, and prints out the following information: 
# The country where the report is from, Total confirmed cases, Total death Total recovered
    
def latest_situation(given_country):
    latest_covid_date = confirmed_clean['Date'].values[-1]
    Total_confirmed_cases = confirmed_clean[(confirmed_clean['Country/Region'] == given_country) & (confirmed_clean['Date'] == latest_covid_date)]['Cases'].sum()
    Total_death_cases = deaths_clean[(deaths_clean['Country/Region'] == given_country) & (deaths_clean['Date'] == latest_covid_date)]['Cases'].sum()
    Total_recoveries_cases = recoveries_clean[(recoveries_clean['Country/Region'] == given_country) & (recoveries_clean['Date'] == latest_covid_date)]['Cases'].sum()
    print("country: ", given_country) 
    print("Total_confirmed_cases: ", Total_confirmed_cases)
    print("Total_death_cases: ", Total_death_cases)
    print("Total_recoveries_cases: ", Total_recoveries_cases)


latest_situation('US') 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function that reports the latest situation of the Corona Virus in a given country. 
# The function takes one argument as input - the country where the report is from, and return/print out the following information: 
# The country where the report is from, Total confirmed cases, Total death Total recovered in a "dataframe"

def latest_situation(given_country):
    
    latest_confirmed_cases = confirmed_clean[confirmed_clean['Date'] == confirmed_clean['Date'].values[-1]]
    latest_death_cases = deaths_clean[deaths_clean['Date'] == deaths_clean['Date'].values[-1]]
    latest_recoveries = recoveries_clean[recoveries_clean['Date'] == recoveries_clean['Date'].values[-1]]

    Total_lastest_confirmed_cases = latest_confirmed_cases.groupby(['Country/Region','Date'])['Cases'].sum().reset_index().rename(columns={'Cases':'Total_confirmed_cases'})
    Total_lastest_death_cases = latest_death_cases.groupby('Country/Region')['Cases'].sum().reset_index().rename(columns={'Cases':'Total_death_cases'})
    Total_lastest_recoveries = latest_recoveries.groupby('Country/Region')['Cases'].sum().reset_index().rename(columns={'Cases':'Total_recovries'})

    Total_lastest_covid_cases = Total_lastest_confirmed_cases.merge(Total_lastest_death_cases, how='inner', on='Country/Region')
    Total_lastest_covid_cases = Total_lastest_covid_cases.merge(Total_lastest_recoveries, how='inner', on='Country/Region')
    
    return print(Total_lastest_covid_cases[Total_lastest_covid_cases['Country/Region'] == given_country])
    
    
latest_situation('US')
                                                            
---------------------------------------------------------  Latest Situation Codes  ------------------------------------------------------------------

latest_confirmed_cases = confirmed_clean[confirmed_clean['Date'] == confirmed_clean['Date'].values[-1]]
latest_death_cases = deaths_clean[deaths_clean['Date'] == deaths_clean['Date'].values[-1]]
latest_recoveries = recoveries_clean[recoveries_clean['Date'] == recoveries_clean['Date'].values[-1]]

---------------------------------------------------------  Latest Situation Codes  ------------------------------------------------------------------
                                                         
#######################################    TEST TEST TES   T##############################################

plt.figure(figsize=(50, 10))
sns.lineplot(data=US_covid_cases, x= 'Date', y= 'Cases')
sns.lineplot(data=Vietnam_covid_cases, x= 'Date', y= 'Cases')

confirmed_clean.info()

Vietnam_covid_cases = confirmed_clean[(confirmed_clean['Country/Region'] == 'Vietnam') & (confirmed_clean['Date'] >= '2022-08-01')]

US_covid_cases = confirmed_clean[(confirmed_clean['Country/Region'] == 'US') & (confirmed_clean['Date'] >= '2022-08-01')]

#######################################    TEST TEST TES   T##############################################
 
---------------------------------------------------------  Data Insights  ------------------------------------------------------------------
   
Until October 31st, 2020, among the top 5 countries (by the current total number of confirmed cases), 
which country(s) should we pay special attention to? 
Support your arguments with further analysis and visualization.

# top 5 countries by the current total number of confirmed cases
top_5_countries = latest_confirmed_cases.groupby('Country/Region')['Cases'].sum().sort_values(ascending=False).head(5).index

# confirmed cases
top5_countries_confirmed_cases = confirmed_clean[confirmed_clean['Country/Region'].isin(top_5_countries) & (confirmed_clean['Date'] < '2020-11-1')]

# deaths cases
top5_countries_death_cases = deaths_clean[deaths_clean['Country/Region'].isin(top_5_countries) & (deaths_clean['Date'] < '2020-11-1')]

# recoveries
top5_countries_recoveries = recoveries_clean[recoveries_clean['Country/Region'].isin(top_5_countries) & (recoveries_clean['Date'] < '2020-11-1')]

# Visualization 
plt.figure(figsize=(30, 8))
plt.subplot(131)
sns.set_style("whitegrid")
sns.lineplot(data=top5_countries_confirmed_cases,
              x='Date',
            y='Cases',
             hue='Country/Region')


plt.title("Confirmed")

sns.set_style("whitegrid")
plt.subplot(132)
sns.lineplot(data=top5_countries_death_cases,
              x='Date',
            y='Cases',
             hue='Country/Region')

plt.title("Deaths")

sns.set_style("whitegrid")
plt.subplot(133)
sns.lineplot(data=top5_countries_recoveries,
              x='Date',
            y='Cases',
             hue='Country/Region')

plt.title("Recoveries")

plt.show()

US_min_number = top5_contries_recoveries[top5_contries_recoveries['Country/Region'] == 'France']['Cases'].min()
US_max_number = top5_contries_death_cases[top5_contries_death_cases['Country/Region'] == 'US']['Cases'].max()

France_Covid_August_cases = top5_contries_confirmed_cases[(top5_contries_confirmed_cases['Country/Region'] == 'France') & (top5_contries_confirmed_cases['Date'] == '2020-08-01')]

Vietnam_covid_cases = confirmed_clean[(confirmed_clean['Country/Region'] == 'Vietnam') & (confirmed_clean['Date'] >= '2022-08-01')]

---------------------------------------------------------  Data Insights  ------------------------------------------------------------------

The line graphs describe the covid cases of the top 5 countries which are US, India, 
Brazil, Germany and France from January 22nd, 2020 to October 31st, 2020. 
Overall, US had the highest Covid cases confirmed and was the country that
suffered mostly from the Covid Pandemic. 

As can be seen, US had reported to have the first case from January 22nd, 2020.
Following this, until April 2020, the number dramatically rised to its peak at 9157419  
and deaths were reported at 230168 in October. August 1st, 2020, 4601257 Covid cases confirmed and 
4174884 cases recovered in October, 2020 which means roughly 90 percent of confirmed cases has recovered  in 3 months

Whereas, the number of Covid cases confirmed in France was reported to have the 
first 3 cases of Covid in January 26th, 2020 and rised steadily to reach its highest at 1374691 
in October. There was only 1 death reported in Feb 20th, 2020 and ended at 36495 death cases in October. 
August 1st, 2020, 215135 Covid cases confirmed and 119653 cases recovered in October, 2020 
which means roughly 55 percent of confirmed cases has recovered in 3 months

---------------------------------------------------------  Data Insights  ------------------------------------------------------------------

US_min_number = top5_contries_recoveries[top5_contries_recoveries['Country/Region'] == 'France']['Cases'].min()
US_max_number = top5_contries_death_cases[top5_contries_death_cases['Country/Region'] == 'US']['Cases'].max()

France_Covid_August_cases = top5_contries_confirmed_cases[(top5_contries_confirmed_cases['Country/Region'] == 'France') & (top5_contries_confirmed_cases['Date'] == '2020-08-01')]

Vietnam_covid_cases = confirmed_clean[(confirmed_clean['Country/Region'] == 'Vietnam') & (confirmed_clean['Date'] >= '2022-08-01')]

---------------------------------------------------------  Data Insights  ------------------------------------------------------------------

# confirmed cases
top5_countries_confirmed_cases = confirmed_clean[confirmed_clean['Country/Region'].isin(top_5_countries) & (confirmed_clean['Date'] >= '2022-01-01') & (confirmed_clean['Date'] < confirmed_clean['Date'].values[-1])]

# deaths cases
top5_countries_death_cases = deaths_clean[deaths_clean['Country/Region'].isin(top_5_countries) & (deaths_clean['Date'] >= '2022-01-01') & (deaths_clean['Date'] < deaths_clean['Date'].values[-1])]

# recoveries
top5_countries_recoveries = recoveries_clean[recoveries_clean['Country/Region'].isin(top_5_countries) & (recoveries_clean['Date'] >= '2022-01-01') & (recoveries_clean['Date'] < recoveries_clean['Date'].values[-1])]

---------------------------------------------------------  US confirmed Data Insights  ------------------------------------------------------------------

US_Covid_latest_cases_data = top5_countries_confirmed_cases[(top5_countries_confirmed_cases['Country/Region'] == 'US') & (top5_countries_confirmed_cases['Date'] == top5_countries_confirmed_cases['Date'].values[-1])]

US_latest_cases = US_Covid_latest_cases_data['Cases'].values

US_1st_2022_data =  top5_countries_confirmed_cases[(top5_countries_confirmed_cases['Country/Region'] == 'US') & (top5_countries_confirmed_cases['Date'] == top5_countries_confirmed_cases['Date'].values[0])]

US_1st_2022_cases = US_1st_2022_data['Cases'].values

number_of_increased_cases = US_latest_cases - US_1st_2022_cases

--------------------------------------------------------- US deaths Data Insights  ------------------------------------------------------------------

US_Covid_latest_cases_data = top5_countries_death_cases[(top5_countries_death_cases['Country/Region'] == 'US') & (top5_countries_death_cases['Date'] == top5_countries_death_cases['Date'].values[-1])]

US_latest_cases = US_Covid_latest_cases_data['Cases'].values

US_1st_2022_data =  top5_countries_death_cases[(top5_countries_death_cases['Country/Region'] == 'US') & (top5_countries_death_cases['Date'] == top5_countries_death_cases['Date'].values[0])]

US_1st_2022_cases = US_1st_2022_data['Cases'].values

number_of_increased_cases = US_latest_cases - US_1st_2022_cases

---------------------------------------------------------  Double Bars Chart Example Codes ------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
times = pd.date_range('2018-09-01', periods=7, freq='5D')
yesSeries = pd.Series([1800,2000,3000,1000,2000,1500,1700], index=times)
nodSeries = pd.Series([200,500,700,600,300,50,0], index=times)

df = pd.DataFrame({"Example one":yesSeries,"Example two":nodSeries})
ax = df.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Epic Graph\nAnother Line! Whoa")
ax.set_xlabel("date")
ax.set_ylabel("counts")
ax.xaxis.set_major_formatter(plt.FixedFormatter(times.strftime("%b %d %Y")))
plt.gcf().autofmt_xdate()
plt.show()

---------------------------------------------------------  Double Bars Chart Example Codes  ------------------------------------------------------------------

---------------------------------------------------------  Double Bars Confirmed Cases Chart  ------------------------------------------------------------------


top5_countries_confirmed_cases = confirmed_clean[(confirmed_clean['Country/Region'].isin(top_5_countries)) & (confirmed_clean['Date'] >= '2022-01-01') & (confirmed_clean['Date'] < confirmed_clean['Date'].values[-1])]

Last_updated_top5_countries_confirmed_cases_2022 = top5_countries_confirmed_cases.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'Latest Cases'})

First_2022_top5_countries_confirmed_cases_2022 = top5_countries_confirmed_cases_2022[top5_countries_confirmed_cases_2022['Date'] == '2022-01-01']
                                                                                             
First_2022_top5_countries_confirmed_cases_2022 = First_2022_top5_countries_confirmed_cases_2022.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'2022-01-01'})   

Double_Bars_Chart_data_frame = Last_updated_top5_countries_confirmed_cases_2022.merge(First_2022_top5_countries_confirmed_cases_2022, how='inner', on ='Country/Region')

Double_Bars_Chart_data_frame = Double_Bars_Chart_data_frame[['Country/Region','2022-01-01', 'Latest Cases']]


ax = Double_Bars_Chart_data_frame.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Confirmed Cases\n2022-01-01 vs 2022-08-09", x='Country/Region')
ax.set_xlabel("Countries")
ax.set_ylabel("Cases")
plt.show()

---------------------------------------------------------  Double Bars Deaths Chart  ------------------------------------------------------------------

top5_countries_death_cases = deaths_clean[(deaths_clean['Country/Region'].isin(top_5_countries)) & (deaths_clean['Date'] >= '2022-01-01') & (deaths_clean['Date'] < deaths_clean['Date'].values[-1])]

Last_updated_top5_countries_death_cases_2022 = top5_countries_death_cases.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'Latest Cases'})

First_2022_top5_countries_death_cases_2022 = top5_countries_death_cases[top5_countries_death_cases['Date'] == '2022-01-01']
                                                                                             
First_2022_top5_countries_death_cases_2022 = First_2022_top5_countries_death_cases_2022.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'2022-01-01'})   

Double_Bars_Chart_deaths = First_2022_top5_countries_death_cases_2022.merge(Last_updated_top5_countries_death_cases_2022, how='inner', on ='Country/Region')

ax_1 = Double_Bars_Chart_deaths.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Death Cases\n2022-01-01 vs 2022-08-09", x='Country/Region')
ax_1.set_xlabel("Countries")
ax_1.set_ylabel("Cases")
plt.show()

---------------------------------------------------------  Double Bars Recoveries Chart  ------------------------------------------------------------------

top5_countries_recoveries_cases = recoveries_clean[(recoveries_clean['Country/Region'].isin(top_5_countries)) & (recoveries_clean['Date'] >= '2022-01-01') & (recoveries_clean['Date'] < recoveries_clean['Date'].values[-1])]

Last_updated_top5_countries_recoveries_cases_2022 = top5_countries_recoveries_cases.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'Latest Cases'})

First_2022_top5_countries_recoveries_cases_2022 = top5_countries_recoveries_cases[top5_countries_recoveries_cases['Date'] == '2022-01-01']
                                                                                             
First_2022_top5_countries_recoveries_cases_2022 = First_2022_top5_countries_recoveries_cases_2022.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'2022-01-01'})   

Double_Bars_recoveries = First_2022_top5_countries_recoveries_cases_2022.merge(Last_updated_top5_countries_recoveries_cases_2022, how='inner', on ='Country/Region')

ax_2 = Double_Bars_recoveries.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Recoveries\n2022-01-01 vs 2022-08-09", x='Country/Region')
ax_2.set_xlabel("Countries")
ax_2.set_ylabel("Cases")
plt.show()

---------------------------------------------------------  China Vs Vietnam Double Bars Chart  ------------------------------------------------------------------

China_Vietnam_confirmed_cases = confirmed_clean[(confirmed_clean['Country/Region'] == 'China') | (confirmed_clean['Country/Region'] == 'Vietnam')]

China_Vietnam_confirmed_cases = China_Vietnam_confirmed_cases[(China_Vietnam_confirmed_cases['Date'] >= '2022-01-01') & (confirmed_clean['Date'] < confirmed_clean['Date'].values[-1])]                                           

China_Vietnam_confirmed_cases = China_Vietnam_confirmed_cases[China_Vietnam_confirmed_cases['Province/State'] != 'Hong Kong']

China = China_Vietnam_confirmed_cases.groupby(['Province/State','Country/Region'])['Cases'].max().reset_index()

China = China.pivot_table(values='Cases',
                          index=['Country/Region','Province/State'],
                          aggfunc='sum',
                          margins=True)

China = China.groupby('Country/Region')['Cases'].max().reset_index()

Vietnam = China_Vietnam_confirmed_cases[China_Vietnam_confirmed_cases['Country/Region'] == 'Vietnam']

Vietnam = Vietnam.groupby('Country/Region')['Cases'].max().reset_index()

China_Vietnam_data = China.merge(Vietnam, how='outer', on='Country/Region')

Double_Bars_recoveries = First_2022_top5_countries_recoveries_cases_2022.merge(Last_updated_top5_countries_recoveries_cases_2022, how='inner', on ='Country/Region')

Last_updated_China_Vietnam_confirmed_cases = China_Vietnam_confirmed_cases.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'Latest Cases'})



First_China_Vietnam_confirmed_cases = China_Vietnam_confirmed_cases[China_Vietnam_confirmed_cases['Date'] == '2022-01-01']

First_China_Vietnam_confirmed_cases = First_China_Vietnam_confirmed_cases.groupby('Country/Region')['Cases'].max().reset_index().rename(columns = {'Cases':'2022-01-01'})   

China_Vietnam_Visualization = First_China_Vietnam_confirmed_cases.merge(Last_updated_China_Vietnam_confirmed_cases, how='inner', on ='Country/Region')

China_Vietnam = China_Vietnam_Visualization.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Confirmed Cases\n2022-01-01 vs 2022-08-09", x='Country/Region')
China_Vietnam.set_xlabel("Countries")
China_Vietnam.set_ylabel("Cases")
plt.show()


df.pivot_table(index=['A', 'B'], 
               values=['C', 'D'], 
               aggfunc=['sum', 'count'], 
               margins=True)

---------------------------------------------------------  China Vs Vietnam Double Bars Chart  ------------------------------------------------------------------

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recoveries = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

identifiers = confirmed.columns[:4]
values = confirmed.columns[4:]

confirmed_clean = confirmed.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

deaths_clean = deaths.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

recoveries_clean = recoveries.melt(id_vars=identifiers,
            value_vars=values, 
            var_name='Date',
            value_name='Cases')

# Convert to proper date and time
confirmed_clean['Date'] = pd.to_datetime(confirmed_clean['Date'])
deaths_clean['Date'] = pd.to_datetime(deaths_clean['Date'])
recoveries_clean['Date'] = pd.to_datetime(recoveries_clean['Date'])



                                                                                                                       