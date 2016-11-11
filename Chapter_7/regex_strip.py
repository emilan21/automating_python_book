#! python3.5
# regex_strip.py - Regex Version of strip()

import re

def strip(string, char_to_strip):
    if char_to_strip == '':
        strip_space = re.compile(r'''(\w+.+)\w''')
        new_string = strip_space.search(string)
        return new_string.group(0)
    else:
        char_strip = re.compile(r':wq
                ')


print('Enter a string')
string = input()
print('Enter a character to strip from the string (Hit enter for space)')
char_to_strip = input()

new_string = strip(string, char_to_strip)
print(new_string)
