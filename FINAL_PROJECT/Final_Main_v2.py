# NAME:                 Gaurav Makin & Anup Kumar
# CLASS:                PYTHON FOR DATA ANALYTICS
# PROJECT OBJECTIVE:    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import warnings

global_temperature_country = pd.read_csv('/Volumes/Gauravs_2nd/CODE/Berekely_Learning/FINAL_PROJECT/GlobalLandTemperaturesByCountry.csv')

countries = np.loadtxt('/Volumes/Gauravs_2nd/CODE/Berekely_Learning/FINAL_PROJECT/Countries.txt', dtype=(str), delimiter='|')
countries = countries[:,1]

global_temperature_country_clear = global_temperature_country[np.isfinite(global_temperature_country['AverageTemperature'])]

# Delete all rows for countries that do not exist in the countries list

#global_temperature_country_clear = global_temperature_country_clear[global_temperature_country_clear['Country'].isin(countries)]
print(global_temperature_country_clear.head(50))