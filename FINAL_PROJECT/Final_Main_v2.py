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
from numpy import unique, loadtxt, isfinite, asarray, polyfit, polyval
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

# Function to generate a curve fit array based on 5th degree polynomial 
def plot_fit_curve(xlist,ylist):
    xarr = asarray(xlist).astype(int)
    yarr = asarray(ylist)
    fit = polyfit(xarr, yarr, 5)
    return polyval(fit, xarr)

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
    ax2.plot(year_list, plot_fit_curve(year_list, max_dict), color = 'g', lw = 1, ls = '-.', label = ('Curve of Maximum temperatures of ' + str(InputCountry)))
    ax2.plot(year_list, min_dict, color = 'blue', lw = 1, ls = '-', label = ('Minimum temperatures of ' + str(InputCountry)))
    ax2.plot(year_list, plot_fit_curve(year_list, min_dict), color = 'k', lw = 1, ls = '-.', label = ('Curve of Minimum temperatures of ' + str(InputCountry)))
    ax2.legend(loc = 0, frameon = False)
    fig2.canvas.set_window_title("Rise in temperatures for %s" % InputCountry)
    plb.xlabel('Years', fontsize = 12, position = (0.005, 0), color = 'black')
    plb.ylabel('Temperature')
    plb.xlim(min(year_list), max(year_list))
    #plb.pause(10)

# Function to convert celcius to Farenheit
def cel_far(temperature):
    far_temp = temperature * 9/5 + 32
    return float(far_temp)

UserCountry = input("Enter Country Name:\t")
max_min_country(UserCountry)

# Global Land Temperature Plot
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
ax.plot(years, plot_fit_curve(years, mean_world), color = 'g', lw = 1, ls = '-', label = 'Curve of Global Mean temperatures')
ax.plot(years, med_world, color = 'blue', lw = 1, ls = '-.', label = 'Global Median Temperatures')
ax.legend(loc = 0, frameon = False)

plb.xlabel('Years')
plb.ylabel('Temperature')
fig.canvas.set_window_title('Global Temperature Rise Year Over Year')
plb.show()