#! python3.6
# filling_gaps.py - Finds all files with the prefix spam001.txt spam002.txt, and so on within a single
# folder. It then locates any gaps in the numbering and renames the files to close the gaps

import os
import shutil
import re

file_regex = re.compile('spam\d\d\d.txt')
find_num_regex = re.compile('(\d)(\d)(\d)')
regex_file_list = []

# Get directory to search from user
print('Enter a directory:')
source_dir = input()

# Make a new list with regex to only find files with a certian pattern
for file_name in  os.listdir(source_dir):
    if file_regex.search(file_name):
        regex_file_list.append(file_name)

# Sort list so that files are sequentual
regex_file_list.sort()
print(regex_file_list)

start_counter =  find_num_regex.search(regex_file_list[0])
counter = start_counter.group(3)
print(counter)

#for file_name in regex_file_list:
#    file_num = find_num_regex.search(file_name)
#    if counter == file_num.group(3):
#        continue
#    else:
#        regex_file_list.nsert(counter, )
