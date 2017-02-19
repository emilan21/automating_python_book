#! python3.5
# backup_to_zip.py - Copies an entire directory and its contents into
# a Zip file whose filename increments.

import zipfile
import os

def backup_to_zip(directory):
    # Backup the entire contents of "folder" into a ZIP file.

    directory = os.path.abspath(directory)    # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(directory) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    # Walk the entire directory tree and compress the files in each directory.
    for folder_name, subfolders, file_names in os.walk(folder):
        print('Adding files in %s...' % (folder_name))
        # Add the current folder to the ZIP file.
        backup_zip.write(folder_name)
        # Add all the files in this folder to the ZIP file.
        for file_name in file_names:
            new_base = os.path.basename(directory) + '_'
            if file_name.startswith(new_base) and file_name.endswith('.zip'):
                continue    # don't backup the backup ZIP files
            backup_zip.write(os.path.join(folder_name, file_name))
    backup_zip.close()
    print('Done.')

backup_to_zip('dates')
