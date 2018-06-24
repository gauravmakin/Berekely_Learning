'''
NAME:                 Gaurav Makin & Anup Kumar

CLASS:                PYTHON FOR DATA ANALYTICS

PROJECT OBJECTIVE:    Analyze weather/temperature data to determine rise in mean annual temperatures for 
                      countries and major cities, tracking how average temperature has changed over the years.
                      To provide a numerical and graphical analysis on global warming (extreme temperatures i.e. hot
                      and cold). 
                      Based on this numerical analysis we will try to extrapolate the temperature in a future period.
'''

import numpy as np
import scipy as sc
import pylab as plb

import pandas as pd
import time
import sys

#print(__doc__)

global_temperature_country = pd.read_csv('/Volumes/Gauravs_2nd/CODE/Berekely_Learning/FINAL_PROJECT/GlobalLandTemperaturesByCountry.csv')

countries = np.loadtxt('/Volumes/Gauravs_2nd/CODE/Berekely_Learning/FINAL_PROJECT/Countries.txt', dtype=(str), delimiter='|')
countries = countries[:,1]

global_temperature_country_clear = global_temperature_country[np.isfinite(global_temperature_country['AverageTemperature'])]

# Delete all rows for countries that do not exist in the countries list
global_temperature_country_clear['Exists'] = global_temperature_country_clear.Country.isin(countries).astype(int)
global_temperature_country_clear = global_temperature_country_clear[global_temperature_country_clear.Exists != 0]
global_temperature_country_clear.drop('Exists', axis = 1, inplace = True)

# Get columns from month and year from the date column
global_temperature_country_clear['Year'] = global_temperature_country_clear['dt'].str[0:4]
global_temperature_country_clear['Month'] = global_temperature_country_clear['dt'].str[5:7]

# Print few lines fo the data frame
print(global_temperature_country_clear.head(5))

# Find avg, max, min temperature for each country each month over the years
countries = np.unique(global_temperature_country_clear['Country'])
mean_temp = []
for i in countries:
    mean_temp.append(global_temperature_country_clear[global_temperature_country_clear['Country'] == i]['AverageTemperature'].mean())

#print(mean_temp)

mean_temp_bar, countries_bar = (list(x) for x in zip(sorted(zip(mean_temp, countries))))


# Find max and min for each month for a country and append to new dataframe object / country
# Define function to convert celcius to farenheit
# Iterate over each countries records to find deviation in max and min temperatures
# Determine how to use scipy libraries
# Plot data in graphs to show mean over the years, max/min changes over the years
# See the global file to see if anything else can be done