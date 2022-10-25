# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:07:12 2022

@author: USER
"""

import pandas as pd

hotel_raw_df = pd.read_csv('C:/Users/USER/.spyder-py3/Project 14 Hotel Booking Demand/hotel_bookings.csv')

'''Content of exploratory data analysis.

Where do the guests come from?

How much do guests pay for a room per night?

How does the price per night vary over the year?

Which are the busiest month?

How long do people stay at the hotels?

Bookings by market segment

How many bookings were canceled?

Which month has the highest number of cancelations?

Repeated guest effect on cancellations.

The number of nights spent at hotels.

Hotel type with more time spent.

Effects of deposit on cancellations by segments.

Relationship of lead time with cancellation.

Monthly customers and cancellations.'''


hotel_raw_df.info()

hotel_raw_df.describe()

# Check the percentage of null values in our data frame. Option 1

null_values = pd.DataFrame({'Null Values' : hotel_raw_df.isna().sum(), 
                            'Percentage Null Values' : round(hotel_raw_df.isna().mean() * 100, 2) })


# Check the percentage of null values in our data frame. Option 2
for column in hotel_raw_df.columns:
    percentage = hotel_raw_df[column].isnull().mean()
    print(f'{column}: {round(percentage*100, 2)}%')

# No booking # No value    
filter = (hotel_raw_df.children == 0) & (hotel_raw_df.adults == 0) & (hotel_raw_df.babies == 0)
hotel_raw_df = hotel_raw_df[~filter]
    
# Exploratory Analysis and Visualization   

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

hotel_raw_df.country.nunique()

top_countries_with_codes = hotel_raw_df.country.value_counts().head(10)

'''PRT — Portugal, GBR — United Kingdom, 
FRA — France, ESP — Spain, DEU — Germany, 
ITA — Italy, IRL — Ireland, BEL — Belgium, 
BRA — Brazil, NLD — Netherlands.'''

plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
plt.title('Top 10 countries from where these hotels are recieving guests')
sns.barplot(x=top_countries_with_codes.index, y=top_countries_with_codes);

# Using another data to get the name of country's code
country_code = pd.read_csv('C:/Users/USER/.spyder-py3/Project 14 Hotel Booking Demand/countries_codes_and_coordinates.csv')

# Check what need to be removed from the dataset
''' Print out the index to check index specificly.
 And using len() to check how many index there are in a string.'''

check_index = []
for i in country_code['Alpha-3 code'][0]:
    check_index .append(i)

# Remove " from the column Alpha-3 code to get only Alphabetical characters. 
country_code['country'] = country_code['Alpha-3 code'].str.replace('"','')

country_code['country'] = country_code['country'].str.replace(' ','')

del country_code['Numeric code']
del country_code['Latitude (average)']
del country_code['Longitude (average)']
del country_code['Alpha-2 code']
del country_code['Alpha-3 code']

hotel_df = pd.merge(hotel_raw_df, country_code) # Both is useable !!!
hotel_df = hotel_raw_df.merge(country_code, how='inner', on='country') # Both is useable !!!

''' Where do the guests come from? '''
top_countries = hotel_df.Country.value_counts().head(10)

plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
plt.title('Top 10 countries from where these hotels are recieving guests')
sns.barplot(x=top_countries.index, y=top_countries_with_codes);
                 
''' How much do guests pay for a room per night? '''

country_wise_guests = hotel_df[hotel_df['is_canceled'] == 0]['Country'].value_counts().reset_index().rename(columns={'Country':'No of guests'})

hotel_df.to_csv('Hotel_booking_analysis.cvs')

hotel_df.info()

import numpy as np

resort_hotel = hotel_df.loc[(hotel_df["hotel"] == "Resort Hotel") & (hotel_df["is_canceled"] == 0)]
city_hotel = hotel_df.loc[(hotel_df["hotel"] == "City Hotel") & (hotel_df["is_canceled"] == 0)]

resort_hotel_filtered = resort_hotel.replace([np.inf, -np.inf], 0)
city_hotel_filtered = city_hotel.replace([np.inf, -np.inf], 0)

resort_hotel["adr_pp"] = resort_hotel["adr"] / (resort_hotel["adults"] + resort_hotel["children"])
city_hotel["adr_pp"] = city_hotel["adr"] / (city_hotel["adults"] + city_hotel["children"])



print("""From all non-cnceled bookings, across all room types and meals, the average prices are:
Resort hotel: {:.2f} € per night and person.
City hotel: {:.2f} € per night and person."""
      .format(resort_hotel_filtered["adr_pp"].mean(), city_hotel_filtered["adr_pp"].mean()))
 

# normalize price per night (adr):
hotel_df["adr_pp"] = hotel_df["adr"] / (hotel_df["adults"] + hotel_df["children"])
hotel_df_guests = hotel_df.loc[hotel_df["is_canceled"] == 0] 
    
    
# only actual guests  
room_prices = hotel_df_guests[["hotel", "reserved_room_type", "adr_pp"]].sort_values("reserved_room_type")

plt.figure(figsize=(14, 10))
sns.boxplot(x="reserved_room_type",
            y="adr_pp",
            hue="hotel",
            data=room_prices, 
            hue_order=["City Hotel", "Resort Hotel"],
            fliersize=0)
plt.title("Price of room types per night and person", fontsize=16)
plt.xlabel("Room type", fontsize=16)
plt.ylabel("Price [EUR]", fontsize=16)
plt.legend(loc="upper right")
plt.ylim(0, 160)
plt.show() 

