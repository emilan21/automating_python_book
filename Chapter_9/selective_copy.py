#! python3.5
# selective_copy.py - Walks through a directory tree and searches for files with a certain file extenison. 
# It then will copy these files from the original location to a new location.

import os
import shutil

def copy_files_with_extension(extension_type, source_dir, des_dir):

    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)

    # Walk the entire directory tree and move files with extension type .pdf
    for folder_name, sub_folders, file_names in os.walk(source_dir):
        print('Looking for %s files in %s...' % (extension_type, folder_name))
        for sub_folder in sub_folders:
            for file_name in file_names:
                if not file_name.endswith(extension_type):
                    continue
                shutil.copy(file_name, des_dir)


# Get file extension, source directory, and desitnation directory
print('Enter a file extension type such as ".pdf" or ".jpg":')
extension = input()
print('Enter a source directory with the files:')
source_dir = input()
print('Enter a destination directory where the file should be copied:')
des_dir = input()
copy_files_with_extension(extension, source_dir, des_dir)
