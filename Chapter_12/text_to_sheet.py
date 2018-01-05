#!/usr/bin/env python

# text_to_sheet.py - Reads in the contents of several text
# files and inserts the contents into a spreadsheet one line
# of text per row. The lines of the first text file will
# be in the cells of column A, the lines of the second text
# files will be in the cells of column B, and so on.abs

# Will use the readlines() File objecto to return a list of
# strings

import openpyxl
import re
import os
import sys

directory_path = sys.argv[1]

# text file regex
text = re.compile(r'\w+.txt')

# create work book# Save workbook
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

# read files in directory
for file in os.listdir(directory_path):
    if text.search(file):
        text_file = open(file, 'r') 
        text_file_content = text_file.readlines()
        for string in text_file_content:
            print(string, end='')
        text_file.close()

# Save workbook
wb.save('text_to_sheet.xlsx')