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
import warnings
import sys

global_temperature_country = pd.read_csv('/Users/gaurav/Documents/LEARNING/GitHub/Berekely_Learning/FINAL_PROJECT/GlobalLandTemperaturesByCountry.csv')

countries = np.loadtxt('/Users/gaurav/Documents/LEARNING/GitHub/Berekely_Learning/FINAL_PROJECT/Countries.txt', dtype=(str), delimiter='|')
countries = countries[:,1]

global_temperature_country_clear = global_temperature_country[np.isfinite(global_temperature_country['AverageTemperature'])]

# Delete all rows for countries that do not exist in the countries list
global_temperature_country_clear['Exists'] = global_temperature_country_clear.Country.isin(countries).astype(int)
global_temperature_country_clear = global_temperature_country_clear[global_temperature_country_clear.Exists != 0]
#print(global_temperature_country_clear.head(50))

print(__doc__)

# Find avg temperature for each month over the years
for x, i in enumerate(global_temperature_country_clear, 0):
    print('DataFrame formation per country per month avg, max, min')
# Find max and min for each month for a country and append to new dataframe object / country
# Define function to convert celcius to farenheit
# Iterate over each countries records to find deviation in max and min temperatures
# Determine how to use scipy libraries
# Plot data in graphs to show mean over the years, max/min changes over the years
# See the global file to see if anything else can be done