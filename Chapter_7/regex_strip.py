#! python3.5
# regex_strip.py - Regex Version of strip()

import re

def strip(string, char_to_strip):
    if char_to_strip == '':
        strip_space = re.compile(r'''(\w.+)\S''')
        new_string = strip_space.search(string)
        return new_string.group(0)
    else:
        char_strip = re.compile(r'[^{0}](.*)[^{0}]'.format(char_to_strip))
        #char_strip = re.compile(r'[^0](.*)[^0]')
        new_string = char_strip.search(string)
        return new_string.group(0)


print('Enter a string')
string = input()
print('Enter a character to strip from the string (Hit enter for space)')
char_to_strip = input()

new_string = strip(string, char_to_strip)
print("\n")
print(new_string)
