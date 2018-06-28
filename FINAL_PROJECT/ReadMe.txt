NAME:               Gaurav Makin & Anup Kumar

CLASS:              PYTHON FOR DATA ANALYTICS

PROJECT OBJECTIVE:  Analyze weather/temperature data to determine rise in mean annual temperatures for 
                    countries and world-wide, tracking how average temperature has changed over the years.
                    To provide a numerical and graphical analysis on global warming (extreme temperatures i.e. hot
                    and cold). 

LIBRARIES REQUIRED: From Pandas, require read_csv
                    from numpy, require loadtxt, unique, isfinite, asarray, polyfit, polyval
                    from os, require path
                    Pylab
                    from pathlib, require Path
                    from warnings, require filterwarnings
                    from scipy, require interpolate

INPUT FILES:        Global Monthly Temperatures per Country.csv
                    Global Monthly Land Temperatures.csv
                    Country list.txt

INPUT FILE FORMAT:  CSV, TXT

PROGRAM FLOW:       Code first reads the file with monthly data for all countries into a dataframe. Once in the dataframe, rows for months with no temperature data
                    are removed. Records for countries that are not listed in the validated list of countries is removed. The data frame is then modified to add coloums
                    for Year and Month from the date field.

                    Dictionary is created from the dataframe with the country name as the key. The Value of each dictionary item is a list that contains values for the average
                    temperature for the country, the maximum and minimum temperatures and the years when the maximum and minimum temperatures occured.

                    Then function is called that requests user input to enter a country name. If found, yearly maximums & minimums of the input country are plotted (X Axis: Year, Y Axis: temperature).
					A function to calculate a curve fit for this data is called and the resulting curve is plotted for max and min temperature. There are two functions to calculate curvefit - one 
					based on numpy using polyfit and the other based on scipy using interpolate. Both curves are plotted.

                    Global monthly file is then read and plotted in the same manner as above to show that over time the average land temperature has increased and is on the upward trend. The function
					to perform curvefit is called again for the mean temperature. A polyfit curve and a interpolate curve is plotted.
					
					Note: This code was built and tested using Python v3.6. The .py file and the data files should be in the same folder. The working directory for code should be same as where the files reside.

EXAMPLE COUNTRY NAMES:  Afghanistan, Albania, Algeria, Argentina, Australia, Austria, Bulgaria, India, United States etc.


  