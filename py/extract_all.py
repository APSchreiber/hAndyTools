# Extract All
# extract_all.py

# Author: Andrew Schreiber
# Created on: 6/11/12
# Updated on 11/9/18

'''
Extracts all files in a directory to the same directory
'''

print "importing modules..."
import os, zipfile, tarfile

# Set variable to the directory that contains the zipped folders
directory_path = r""


files_list = os.listdir(directory_path)
for the_file in files_list:

    if the_file[-3:].lower() == "zip":

##    # check if it is a tar.gz file
##    if ".gz" in the_file:
##        tar = tarfile.open(directory_path + os.sep + the_file, 'r:gz')
##        for item in tar:
##            tar.extract(item)
##        continue
        
    
        file_path = directory_path + os.sep + the_file
        file_ref = zipfile.ZipFile(file_path, "r")
        zip_to_directory = file_path[:-4]
        print "\nextracting " + the_file + " to directory '" + zip_to_directory + "'."
        file_ref.extractall(zip_to_directory)
        file_ref.close()

print "\nscript completed successfully."
