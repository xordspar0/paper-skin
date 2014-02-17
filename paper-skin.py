#! /usr/bin/env python3

import os, sys
from PIL import Image, ImageDraw

# coordinates of the parts in the skin file
skinCoords = [(8,0,16,8), (0,8,32,16), (16,0,24,8), # head
              (4,16,8,20), (0,20,16,32), (8,16,12,20), # legs
              (20,16,28,20), (16,20,40,32), (28,16,36,20), # body
              (44,16,48,20), (40,20,56,32), (48,16,52,20)] # arms

# sizes of the parts after being scaled
newSizes = [(384,384), (1536,384), (384,384), # head
            (192,192), (768,576), (192,192), # legs
            (384,192), (1152,576), (384,192), # body
            (192,192), (768,576), (192,192)] # arms

if len(sys.argv) != 3:
	print("usage: " + sys.argv[0] + " SKIN_FILE OUTPUT_FILE")
	sys.exit(1)

#
# Open the skin file
#
try:
	skin=Image.open(sys.argv[1])
except IOError:
	print("The file " + sys.argv[1] + " does not exist.")
	sys.exit(1)

#
# Create a new image
#
if os.path.isfile(sys.argv[2]):
	print("The file " + sys.argv[2] + " already exists.")
	sys.exit(1)

printable = Image.new("RGB", (2550, 3300), (255, 255, 255))

#
# Draw the borders
#

#
# Cut out sections of the skin file, scale them, and paste them into our image
#

#
# Save the image
#
# (make sure that the file we're writing to still doesn't exist)
printable.show()
