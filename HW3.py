# Homework 3
# Prepared by Maksym Bilyi, id:101169

# Step 1: importing libraries
import subprocess
import os

# Step 2: defining path + using simple -du -sh subprocesses to get the total size + using os for listing folder's items
path = '/Users/macbook/Desktop/SGH'
size = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
list_of_items = os.listdir(path)

# Step 3: printing results
print("Folder size: " + size)
print("List of files and subfolders: " + str(list_of_items))

# Results:
# Folder size: 194M
# List of files and subfolders: ['Males.xls', '.DS_Store', 'Financial Fraud, module 2, Maksym Bilyi copy.docx', 'Financial Fraud, module 2, Maksym Bilyi copy.pdf', 'Kaggle pjs', 'nlswork.dta', 'I semester', 'II semester', 'Financial Fraud, module 1, Maksym Bilyi.docx', 'III semester']