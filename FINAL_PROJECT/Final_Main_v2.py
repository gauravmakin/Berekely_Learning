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
from os import path
import collections
import pandas as pd
import time
import sys
from pathlib import Path

#print(__doc__)

# Find current working directory
my_path = path.dirname(path.abspath(__file__))

temp_data_file = my_path + "//" + "GlobalLandTemperaturesByCountry.csv"
cntry_data_file = my_path + "//" + "Countries.txt"

def file_exists(fname):
    file = Path(fname)
    if file.is_file():
        return True
    else:
        print("Data file " + fname + " not found")
        print("Please check data file path and try again!!")
        exit()
        return False

if file_exists(temp_data_file):
    global_temperature_country = pd.read_csv(temp_data_file)

if file_exists(cntry_data_file):
    countries = np.loadtxt(cntry_data_file, dtype=(str), delimiter='|')

countries = countries[:,1]

global_temperature_country_clear = global_temperature_country[np.isfinite(global_temperature_country['AverageTemperature'])]

# Delete all rows for countries that do not exist in the countries list
global_temperature_country_clear['Exists'] = global_temperature_country_clear.Country.isin(countries).astype(int)
global_temperature_country_clear = global_temperature_country_clear[global_temperature_country_clear.Exists != 0]
global_temperature_country_clear.drop('Exists', axis = 1, inplace = True)

# Get columns from month and year from the date column
global_temperature_country_clear['Year'] = global_temperature_country_clear['dt'].str[0:4]
global_temperature_country_clear['Month'] = global_temperature_country_clear['dt'].str[5:7]

# Print few lines fo the data frame for testing
print(global_temperature_country_clear.head(5))

# Find max, min temperature for each country and in which year did that occur
countries = np.unique(global_temperature_country_clear['Country'])

mean_dict = {}

for i in countries:
    key_name = str(i)
    max_temp = global_temperature_country_clear[global_temperature_country_clear['Country'] == i]['AverageTemperature'].max()
    min_temp = global_temperature_country_clear[global_temperature_country_clear['Country'] == i]['AverageTemperature'].min()
    mean_temp = global_temperature_country_clear[global_temperature_country_clear['Country'] == i]['AverageTemperature'].mean()
    max_year = int(global_temperature_country_clear[global_temperature_country_clear['AverageTemperature'] == max_temp]['Year'].max())
    min_year = int(global_temperature_country_clear[global_temperature_country_clear['AverageTemperature'] == min_temp]['Year'].max())

    mean_dict[key_name] = [max_year, max_temp, min_year, min_temp, mean_temp]

# Function to convert celcius to Farenheit
def Cel_Far(temperature):
    far_temp = temperature * 9/5 + 32
    return float(far_temp)

# Output
def get_maxmin(YourCountry='United States'):
    print(YourCountry + ' :')
    print('\tMaximum temperature of %5.2f was in the year %i' % (mean_dict[YourCountry][1],  mean_dict[YourCountry][0]))
    print('\tMinimum temperature of %5.2f was in the year %i' % (mean_dict[YourCountry][3],  mean_dict[YourCountry][2]))


get_maxmin()    
    

# Iterate over each countries records to find deviation in max and min temperatures
# Determine how to use scipy libraries
# Plot data in graphs to show mean over the years, max/min changes over the years
# See the global file to see if anything else can be done 