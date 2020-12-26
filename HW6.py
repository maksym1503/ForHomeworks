# Homework 6 for Python programming class
# Prepared by Maksym Bilyi, id: 101169


# Step 1:
# Downloading IBM stocks to local drive from: https://finance.yahoo.com/quote/IBM/history?ltr=1
# Current path as follows: /Users/macbook/Desktop/PythonHW/IBM.csv
# The same for MSFT stocks

# Step 2: Checking how many CSV files are in folder

import glob
for files in glob.glob("/Users/macbook/Desktop/PythonHW/*.csv"):
    if files.count('.') == 1:
       print(files)

# This solution will print out only CSV files, so you can easily find those you want to use

# Step 3: importing needed CSV files

import pandas as pd
ibm = pd.read_csv('/Users/macbook/Desktop/PythonHW/IBM.csv')
msft = pd.read_csv('/Users/macbook/Desktop/PythonHW/MSFT.csv')

# Step 3.1: investigating datasets

ibm.isnull().sum()
msft.isnull().sum()
ibm.dtypes
msft.dtypes

# No issues found to be fixed

# Step 4: Calculating the daily percentage change

ibm['Perc_Change'] = (ibm['Close']-ibm['Open'])/ibm['Open']
msft['Perc_Change'] = (msft['Close']-msft['Open'])/msft['Open']

# Step 5: visualizing and otputting results

import matplotlib as plot
ibm['Perc_Change'].plot(figsize = (12, 6), fontsize = 10)
msft['Perc_Change'].plot(figsize = (12, 6), fontsize = 10)

ibm.Perc_Change.describe()
msft.Perc_Change.describe()