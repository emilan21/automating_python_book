#!/usr/bin/python3.5

# decrypt_pdf.py - Will go through a folder and all subfolders looking for all encypted PDF files.
# Will then create a decrypted cope of the PDF files using a password provided on the cli.
# If the password is wrong print a message to the user and continue to the next PDF.abs

import PyPDF2
import os
import sys
import re

file_name_reg = re.compile(r'''(.*)(_encrypted.pdf)''')

password = sys.argv[1]
directory_path = sys.argv[2]

# Get all the PDF filenames.
pdf_files = []
for root, sub_folders, file_names in os.walk(directory_path):
    for file_name in file_names:
        file_name = os.path.join(root, file_name)
        if  os.path.exists(file_name) and file_name.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(open(file_name, 'rb'))
            if pdf_reader.isEncrypted:
                pdf_files.append(file_name)

pdf_files.sort(key=str.lower)

# Got through each pdf in pdf_files and make a new decrypted pdf file.
for file_name in pdf_files:
    base_file_name = os.path.basename(file_name)
    file_path = os.path.dirname(os.path.abspath(file_name))
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader.decrypt(password)
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))
    if base_file_name.endswith('_encrypted.pdf'):
        reg_file_name = file_name_reg.search(base_file_name)
        new_file_name = reg_file_name.group(1)
    else:
        new_file_name = os.path.splitext(base_file_name)[0]
    new_file_name = new_file_name + '.pdf'
    print(new_file_name)
    result_pdf = open(os.path.join(file_path, new_file_name), 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()