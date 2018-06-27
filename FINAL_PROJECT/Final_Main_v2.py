'''
NAME:                 Gaurav Makin & Anup Kumar

CLASS:                PYTHON FOR DATA ANALYTICS

PROJECT OBJECTIVE:    Analyze weather/temperature data to determine rise in mean annual temperatures for 
                      countries and major cities, tracking how average temperature has changed over the years.
                      To provide a numerical and graphical analysis on global warming (extreme temperatures i.e. hot
                      and cold). 
'''


import sys
from os import path
from pathlib import Path
from warnings import filterwarnings
from numpy import unique, loadtxt, isfinite
from pandas import read_csv, Series
import pylab as plb
from collections import OrderedDict
import scipy as sc

filterwarnings("ignore")

# Print docstring - Objective etc
print(__doc__)

# ----- FILE HANDLING -----
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
    glbl_temp_cntry = read_csv(temp_data_file)
if file_exists(cntry_data_file):
    countries = loadtxt(cntry_data_file, dtype = (str), delimiter = '|')


# ------ DATA CLEANING -----
    # Get list of valid Countries
countries = countries[:, 1]
    # Clean dataset to remove null entries
glbl_temp_cleaned = glbl_temp_cntry[isfinite(glbl_temp_cntry['AverageTemperature'])]

    # Delete all rows for countries that do not exist in the countries list
glbl_temp_cleaned['Exists'] = glbl_temp_cleaned.Country.isin(countries).astype(int)
glbl_temp_cleaned = glbl_temp_cleaned[glbl_temp_cleaned.Exists != 0]
glbl_temp_cleaned.drop('Exists', axis = 1, inplace = True)
glbl_temp_cntry.reset_index(inplace = True)

    # Get columns from month and year from the date column
glbl_temp_cleaned['Year'] = glbl_temp_cleaned['dt'].str[0:4]
glbl_temp_cleaned['Month'] = glbl_temp_cleaned['dt'].str[5:7]


# ----- DATA ANALYSIS -----
    # Find max, min temperature for each country and in which year did that occur
countries = unique(glbl_temp_cleaned['Country'])
mean_dict = {}

    # Get max, min, years for each country
for i in countries:
    key_name = str(i)
    max_temp = glbl_temp_cleaned[glbl_temp_cleaned['Country'] == i]['AverageTemperature'].max()
    min_temp = glbl_temp_cleaned[glbl_temp_cleaned['Country'] == i]['AverageTemperature'].min()
    mean_temp = glbl_temp_cleaned[glbl_temp_cleaned['Country'] == i]['AverageTemperature'].mean()
    max_year = int(glbl_temp_cleaned[glbl_temp_cleaned['AverageTemperature'] == max_temp]['Year'].max())
    min_year = int(glbl_temp_cleaned[glbl_temp_cleaned['AverageTemperature'] == min_temp]['Year'].max())

    mean_dict[key_name] = [max_year, max_temp, min_year, min_temp, mean_temp]

# Plotting based on user input country
years = unique(glbl_temp_cleaned['Year'])
year_list = years.tolist()

def max_min_country(InputCountry):
    max_dict = []
    min_dict = []
    
    print ("Maximum Temperature of: ", float(mean_dict[InputCountry][1]), ' degree celcius Or ', cel_far(float(mean_dict[InputCountry][1])), 'Farenheit')
    print ('Minimum Temperature of: ', float(mean_dict[InputCountry][3]), ' degree celcius Or ', cel_far(float(mean_dict[InputCountry][3])), 'Farenheit')
    print ('Average Temperature of: ', float(mean_dict[InputCountry][4]), ' degree celcius Or ', cel_far(float(mean_dict[InputCountry][4])), 'Farenheit')
    
    for x in years:
        max_temp = glbl_temp_cleaned[(glbl_temp_cleaned['Country'] == InputCountry) & (glbl_temp_cleaned['Year'] == x)]['AverageTemperature'].max()
        min_temp = glbl_temp_cleaned[(glbl_temp_cleaned['Country'] == InputCountry) & (glbl_temp_cleaned['Year'] == x)]['AverageTemperature'].min()
        if max_temp > 0 or max_temp < 0:
            max_dict.append(max_temp)
            min_dict.append(min_temp)
        else:
            year_list.remove(x)
            continue

    # Plotting the graph for maximum and average temperatures
    fig2 = plb.figure()
    ax2 = fig2.add_axes([0, 0, 1, 1])
    ax2.plot(year_list, max_dict, color = 'red', lw = 1, ls = '-', label = ('Maximum temperatures of ' + str(InputCountry)))
    ax2.plot(year_list, min_dict, color = 'blue', lw = 1, ls = '-', label = ('Minimum temperatures of ' + str(InputCountry)))
    ax2.legend(loc = 0, frameon = False)
    fig2.canvas.set_window_title("Rise in temperatures for %s" % InputCountry)
    plb.xlabel('Years', fontsize = 12, position = (0.005, 0), color = 'black')
    plb.ylabel('Temperature')
    plb.xlim(min(year_list), max(year_list))
    plb.yticks(plb.linspace(0, 50, 10))
    plb.axis('auto')
    plb.pause(2)

# Function to convert celcius to Farenheit
def cel_far(temperature):
    far_temp = temperature * 9/5 + 32
    return float(far_temp)

UserCountry = input("Enter Country Name:\t")

if UserCountry.title() in mean_dict.keys():
    max_min_country(UserCountry.title())
else:
    again = input("Country not found in the dataset. Do you wish to try again? y/n ")
    if again.lower() == 'y':
        UserCountry = input("Enter Country Name:\t")
        max_min_country(UserCountry.title())
    else:
        print('Sorry option not recognized. \nPlotting Yearly Global Temperatures')

#_____________________________________-
# # Create Country specific data
# ctry_df = glbl_temp_cleaned.loc[glbl_temp_cleaned['Country'] == UserCountry]

# # Filter out data earlier than year 2000
# # ctry_df = ctry_df.loc[ctry_df['dt'] >= '2000-01-01']

# # Append summary stats for each country to this data set
# ctry_df['max_year'] = Series(mean_dict['India'][0], index = ctry_df.index)
# ctry_df['max_temp'] = Series(mean_dict['India'][1], index = ctry_df.index)
# ctry_df['min_year'] = Series(mean_dict['India'][2], index = ctry_df.index)
# ctry_df['min_temp'] = Series(mean_dict['India'][3], index = ctry_df.index)
# ctry_df['mean_temp'] = Series(mean_dict['India'][4], index = ctry_df.index)

# # Plot the data for a country  ** Commented out as this plot takes a long time.
# # plb.figure(1)
# # plb.title("Temperature variance by date for %s" % UserCountry )

# # #plb.subplot(2,1,1)
# # plb.plot(ctry_df['dt'], ctry_df['AverageTemperature'],color='blue', linewidth = 1.5, linestyle = '-')
# # plb.plot(ctry_df['dt'], ctry_df['max_temp'] ,color='red', linewidth = 1.2, linestyle = '-.')
# # plb.plot(ctry_df['dt'], ctry_df['min_temp'] ,color='green', linewidth = 1.2, linestyle = '-.')
# # plb.plot(ctry_df['dt'], ctry_df['mean_temp'] ,color='yellow', linewidth = 1.2, linestyle = '-.')

# # plb.pause(5)

# ctry_summ_df = ctry_df[['Year', 'Month', 'AverageTemperature']]
# ctry_summ_df['max_temp'] = ctry_df[['Year', 'AverageTemperature']].groupby(['Year']).max()
# ctry_summ_df['min_temp'] = ctry_df[['Year', 'AverageTemperature']].groupby(['Year']).min()
# ctry_summ_df['mean_temp'] = ctry_df[['Year', 'AverageTemperature']].groupby(['Year']).mean()
# ctry_summ_df.reset_index()

# plb.figure(2)
# plb.title("Temperature variance by years for %s" % UserCountry )

# plb.subplot(2, 1, 1)
# # plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['AverageTemperature'],color='blue', linewidth = 1.5, linestyle = '-')
# # plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['max_temp'] ,color='red', linewidth = 1.2, linestyle = '-.')
# # plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['mean_temp'] ,color='yellow', linewidth = 1.2, linestyle = '-.')

# plb.plot(ctry_summ_df['Year'], ctry_summ_df['AverageTemperature'], color = 'blue', linewidth = 1.5, linestyle = '-')
# plb.plot(ctry_summ_df['Year'], ctry_summ_df['max_temp'] , color = 'red', linewidth = 1.2, linestyle = '-.')
# plb.plot(ctry_summ_df['Year'], ctry_summ_df['mean_temp'] , color = 'yellow', linewidth = 1.2, linestyle = '-.')

# plb.grid()
# # plb.xticks(plb.linspace(1700,2100,50, endpoint=True))
# # plb.yticks(plb.linspace(5,35,5, endpoint=True))

# plb.subplot(2, 1, 2)
# plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['AverageTemperature'], color = 'blue', linewidth = 1.5, linestyle = '-')
# plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['min_temp'] , color = 'green', linewidth = 1.2, linestyle = '-.')
# plb.plot(ctry_summ_df.reset_index()['Year'], ctry_summ_df['mean_temp'] , color = 'yellow', linewidth = 1.2, linestyle = '-.')
# plb.grid()
# # plb.xticks(plb.linspace(1700,2100,50, endpoint=True))
# # plb.yticks(plb.linspace(5,35,5, endpoint=True))

# plb.pause(5)

# # Iterate over each countries records to find deviation in max and min temperatures
# # Determine how to use scipy libraries
# # Plot data in graphs to show mean over the years, max/min changes over the years
# # See the global file to see if anything else can be done 
# ______________________________________________
# plb.pause(2)

# # Global Land Temperature Plot
if file_exists(temp_glb_file):
    glbl_tmp = read_csv(temp_glb_file)

years = unique(glbl_tmp['dt'].apply(lambda x: x[:4]))
mean_world = []
med_world = []

for year in years:
    mean_world.append(glbl_tmp[glbl_tmp['dt'].apply(lambda x: x[:4]) == year]['LandAverageTemperature'].mean())
    med_world.append(glbl_tmp[glbl_tmp['dt'].apply(lambda x: x[:4]) == year]['LandAverageTemperature'].median())

# Plotting the values
fig = plb.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(years, mean_world, color = 'red', lw = 2, ls = '-', label = 'Global Mean Temperatures')
ax.plot(years, med_world, color = 'blue', lw = 1, ls = '-.', label = 'Global Median Temperatures')
ax.legend(loc = 0, frameon = False)

plb.xlabel('Years')
plb.ylabel('Temperature')
plb.axis('auto')
fig.canvas.set_window_title('Global Temperature Rise Year Over Year')
plb.pause(3)