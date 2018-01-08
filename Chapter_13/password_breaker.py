#!/usr/bin/python3.5

# password_breaker.py - Will try to decrypt a pdf file by reading in a text file with dictionary words.
# One word per line. If the word isn't the password it will keep going. If the word is the password
# it will be printed to the screen.

import PyPDF2
import sys

# Get input
text_file_name = sys.argv[1]
pdf_file_name = sys.argv[2]

# Open text file for reading
text_file = open(text_file_name, 'r') 
text_file_content = text_file.readlines()

# Go through text file line by line to see if the string will decrypt the pdf file
for string in text_file_content:
    pdf_file = open(pdf_file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    string = string.rstrip()
    if pdf_reader.decrypt(string) == 1:
        print(string)
        break

# Close the text file
text_file.close()