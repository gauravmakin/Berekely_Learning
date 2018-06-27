NAME:               Gaurav Makin & Anup Kumar

CLASS:              PYTHON FOR DATA ANALYTICS

PROJECT OBJECTIVE:  Analyze weather/temperature data to determine rise in mean annual temperatures for 
                    countries and major cities, tracking how average temperature has changed over the years.
                    To provide a numerical and graphical analysis on global warming (extreme temperatures i.e. hot
                    and cold). 

LIBRARIES REQUIRED: From Pandas, require read_csv, Series
                    from numpy, require loadtxt, unique, isfinite
                    from os import path
                    from pylab as plb
                    from pathlib, require Path
                    from warnings, require filterwarnings
                    import sys to print docstring
                    from scipy as sc
                    
                    import collections

INPUT FILES:        Global Monthly Temperatures per Country
                    Global Monthly Land Temperatures
                    Country list

INPUT FILE FORMAT:  CSV, TXT

PROGRAM FLOW:       Code first reads the file with monthly data for all countries into a dataframe. Once in the dataframe, rows for months with no temperature data
                    are removed. Records for countries that are not listed in the validated list of countries is removed. The data frame is then modified to add coloums
                    for Year and Month from the date field.

                    Dictionary is created from the dataframe with the country name as the key. The Value of each dictionary item is a list that contains values for the average
                    temperature for the country, the maximum and minimum temperatures and the years when the maximum and minimum temperatures occured.

                    Then function is called that requests user input to enter a country name. If found, yearly maximums & maximums of the input country are plotted (X Axis: Year, Y Axis: temperature)

                    Global monthly file is then read and plotted in the same manner as above to show that over time the average land temperature has increased and is on the upward trend


  