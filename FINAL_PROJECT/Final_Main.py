# NAME:         Gaurav Makin & Anup Kumar
# OBJECTIVE:    Temperature Data Analysis
#

import pandas as pnd
from os import listdir

raw_file = pnd.read_csv("FINAL_PROJECT/TEMP_DATA.csv")
print(raw_file.head(15))


