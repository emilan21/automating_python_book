#! python3.5
# regex_search.py - Searches all .txt files in directory for user-supplied regular expression.
# It then prints the results to the screnn

import os
import re

final_list = []

# text file regex
text = re.compile(r'\w+.txt')

# get input
print('Enter regular expression to search for:')
regex_input = input()
print('\n')
user_regex = re.compile('{0}'.format(regex_input))

for file in os.listdir('.'):
    if text.search(file):
        text_file = open(file, 'r')
        text_file_content = text_file.readlines() 
        for string in text_file_content:
            if user_regex.search(string):
                final_list.append(string)
        text_file.close()

for string in final_list:
    print(string, end='')
