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

# Print docstring - Objective etc
#print(__doc__)

# Find current working directory
my_path = path.dirname(path.abspath(__file__))

temp_data_file = path.join(my_path , "GlobalLandTemperaturesByCountry.csv")
cntry_data_file = path.join(my_path , "Countries.txt")
temp_glb_file = path.join(my_path , "GlobalTemperatures.csv")

# Function for handlng data files
def file_exists(fname):
    file = Path(fname)
    if file.is_file():
        return True
    else:
        print("Data file " + fname + " not found")
        print("Please check data file path and try again!!")
        exit()

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

#UserCountry = input("Enter Country Name (Default = United States) : ")
UserCountry = 'India'
get_maxmin(UserCountry)

#Create Country specific data
ctry_df = global_temperature_country_clear.loc[global_temperature_country_clear['Country'] == UserCountry]

#Filter out data earlier than year 2000
#ctry_df = ctry_df.loc[ctry_df['dt'] >= '2000-01-01']

#Append summary stats for each country to this data set
ctry_df['max_year'] = pd.Series(mean_dict['India'][0], index=ctry_df.index)
ctry_df['max_temp'] = pd.Series(mean_dict['India'][1], index=ctry_df.index)
ctry_df['min_year'] = pd.Series(mean_dict['India'][2], index=ctry_df.index)
ctry_df['min_temp'] = pd.Series(mean_dict['India'][3], index=ctry_df.index)
ctry_df['mean_temp'] = pd.Series(mean_dict['India'][4], index=ctry_df.index)

# Plot the data for a country  ** Commented out as this plot takes a long time.
# plb.figure(1)
# plb.title("Temperature variance by date for %s" % UserCountry )

# #plb.subplot(2,1,1)
# plb.plot(ctry_df['dt'], ctry_df['AverageTemperature'],color='blue', linewidth = 1.5, linestyle = '-')
# plb.plot(ctry_df['dt'], ctry_df['max_temp'] ,color='red', linewidth = 1.2, linestyle = '-.')
# plb.plot(ctry_df['dt'], ctry_df['min_temp'] ,color='green', linewidth = 1.2, linestyle = '-.')
# plb.plot(ctry_df['dt'], ctry_df['mean_temp'] ,color='yellow', linewidth = 1.2, linestyle = '-.')

# plb.pause(5)

ctry_summ_df = ctry_df[['Year','Month','AverageTemperature']]
ctry_summ_df['max_temp'] = ctry_df[['Year','AverageTemperature']].groupby(['Year']).max()
ctry_summ_df['min_temp'] = ctry_df[['Year','AverageTemperature']].groupby(['Year']).min()
ctry_summ_df['mean_temp'] = ctry_df[['Year','AverageTemperature']].groupby(['Year']).mean()
ctry_summ_df.reset_index()

plb.figure(2)
plb.title("Temperature variance by years for %s" % UserCountry )

plb.subplot(2,1,1)
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['AverageTemperature'],color='blue', linewidth = 1.5, linestyle = '-')
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['max_temp'] ,color='red', linewidth = 1.2, linestyle = '-.')
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['mean_temp'] ,color='yellow', linewidth = 1.2, linestyle = '-.')
plb.grid()
plb.xticks(plb.linspace(1700,2100,50, endpoint=True))
plb.yticks(plb.linspace(5,35,5, endpoint=True))

plb.subplot(2,1,2)
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['AverageTemperature'],color='blue', linewidth = 1.5, linestyle = '-')
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['min_temp'] ,color='green', linewidth = 1.2, linestyle = '-.')
plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['mean_temp'] ,color='yellow', linewidth = 1.2, linestyle = '-.')
plb.grid()
plb.xticks(plb.linspace(1700,2100,50, endpoint=True))
plb.yticks(plb.linspace(5,35,5, endpoint=True))

plb.pause(5)

# Iterate over each countries records to find deviation in max and min temperatures
# Determine how to use scipy libraries
# Plot data in graphs to show mean over the years, max/min changes over the years
# See the global file to see if anything else can be done 



#global_temp = pd.read_csv('../GlobalTemperatures.csv')
if file_exists(temp_glb_file):
    glbl_tmp = pd.read_csv(temp_glb_file)

years = np.unique(glbl_tmp['dt'].apply(lambda x: x[:4]))
mean_temp_world = []
mean_temp_world_uncertain = []

for year in years:
    mean_temp_world.append(glbl_tmp[glbl_tmp['dt'].apply(lambda x: x[:4]) == year]['LandAverageTemperature'].mean())


print(type(mean_temp_world))


