#!/usr/bin/python3.5

# encrypt_pdf.py - Script will go through every pdf file in a folder and subfolders then encrypt the pdfs using a password
# from the cli. Files will have _encrypted.pdf suffix added to the original file name. Before deleting the orignal file
# the script will attempt to read and decrypt the file to ensure it was encrypted correctly.abs

import PyPDF2
import os
import sys

password = sys.argv[1]
directory_path = sys.argv[2]

# Get all the PDF filenames.
pdf_files = []
for root, sub_folders, file_names in os.walk(directory_path):
    for file_name in file_names:
        file_name = os.path.join(root, file_name)
        print(file_name)
        if  os.path.exists(file_name) and file_name.endswith('.pdf') and not file_name.endswith('_encrypted.pdf'):
            pdf_files.append(file_name)

pdf_files.sort(key=str.lower)
print(pdf_files)

# Got through each pdf in pdf_files and make a new encyrpted pdf file. Then delete old PDF files
for file_name in pdf_files:
    base_file_name = os.path.basename(file_name)
    file_path = os.path.dirname(os.path.abspath(file_name))
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))
    pdf_writer.encrypt(password)
    result_pdf = open(os.path.join(file_path, os.path.splitext(base_file_name)[0]) + '_encrypted.pdf', 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()

    print("Removing " + base_file_name)
    os.remove(os.path.join(file_path, base_file_name))
    print("File removed")
