#! python3.5
# deleting_unneeded_files.py - Walks through a directory tree and searches for exceptionally
# large files or directorys. User can input size to look for. The program will then print them
# to the screen

import os

def find_large_files_and_directories(source_dir, size):
   
    source_dir = os.path.abspath(source_dir)

    # Walk the entire directory tree. Looking for files and directories as large or larger than max_size
    for root, sub_folders, file_names in os.walk(source_dir):

        for file_name in file_names:
            file_name = os.path.join(root, file_name)
            if  os.path.exists(file_name) and os.path.getsize(file_name) >= size:
                print('The file "%s" is larger than %d!!!' % (file_name, size))

print('Enter a directory to search for large files and directories:')
source_dir = input()
print('Enter the size to look for in megabytes:')
size = input()
size = int(size)
size = size * 1024 * 1024
find_large_files_and_directories(source_dir, size)
