#!/usr/bin/python
# filling_gaps.py - Finds all files with the prefix spam001.txt spam002.txt, and so on within a single
# folder. It then locates any gaps in the numbering and renames the files to close the gaps

import os
import shutil
import re

file_regex = re.compile('spam(\d)(\d)(\d).txt')
regex_file_list = []
hun_count = 0
ten_count = 0
single_count = 1

# Get directory to search from user
print('Enter a directory:')
source_dir = input()

# Make a new list with regex to only find files with a certian pattern
for file_name in  os.listdir(source_dir):
    if file_regex.findall(file_name):
        regex_file_list.append(file_name)

# Sort list so that files are sequential
regex_file_list.sort()

# check if there are gaps in list order
for file_name in regex_file_list:
    m = file_regex.match(file_name)
    if hun_count > 9:
        hun_count = 0
    if ten_count > 9:
        ten_count = 0
    if single_count > 9:
        single_count = 0

    for hun in m.group(1):
        if hun_count != int(hun):
            hun = hun_count
            hun_count += 1
        for ten in m.group(2):
            if ten_count != int(ten):
                ten = ten_count
                ten_count += 1
            for single in m.group(3):
                if single_count != int(single):
                    single = single_count
                single_count += 1

    shutil.copy('spam/' + m.group(0), 'spam_test/' + 'spam' + str(hun) + str(ten) + str(single) + '.txt')
