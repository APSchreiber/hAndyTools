# Read EXIF
# read_exif.py

# Author: Andrew Schreiber
# Created: 10/21/13
# Modified: 11/09/18

'''
Reads and prints EXIF data from a directory of pictures
'''

print "importing modules..."
import os, sys, glob
from PIL import Image
from PIL.ExifTags import TAGS

##############################################

working_dir = r""

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

##############################################

os.chdir(working_dir)

for fn in glob.glob(os.path.join(working_dir, "*.jpg")):
    x = get_exif(fn)
    for a in x:
        print a, x[a]
    print
    print "\n-----------------------\n"
    print
