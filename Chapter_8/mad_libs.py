#!python3.5
# mad_libs.py - Lets the user add their own text anywhere the work ADJECTIVE, NOUN, ADVERB, OR VERB
# appers in a text file.

import os
import re

# get file from user
print('Enter the name of a text file')
text_file = input()

# open text file
file = open(text_file, 'r')

# read contents of file
file_content = file.read()

file.close()

# regex input
adjective_reg = re.compile('ADJECTIVE')
noun_reg = re.compile('NOUN')
adverb_reg = re.compile('ADVERB')
verb_reg = re.compile('VERB')

for word in file_content.split():
    if adjective_reg.search(word):
        print('Enter an adjective:')
        replacement = input()
        file_content = file_content.replace(word, replacement, 1)
    if noun_reg.search(word):
        print('Enter a noun:')
        replacement = input()
        file_content = file_content.replace(word, replacement, 1)
    if adverb_reg.search(word):
        print('Enter an adverb:')
        replacement = input()
        file_content = file_content.replace(word, replacement, 1)
    if verb_reg.search(word):
        print('Enter a verb:')
        replacement = input()
        file_content = file_content.replace(word, replacement, 1)

print('\n')
print(file_content)

file = open(text_file, 'w')
file.write(file_content)
file.close()
