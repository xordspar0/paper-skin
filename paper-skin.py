#! /usr/bin/env python3

import os, sys
from PIL import Image, ImageDraw

# coordinates of the parts in the skin file
skinCoords = [(8,0,16,8), (0,8,32,16), (16,0,24,8), # head
              (20,16,28,20), (16,20,40,32), (28,16,36,20), # body
              (44,16,48,20), (40,20,56,32), (48,16,52,20), # arms
              (4,16,8,20), (0,20,16,32), (8,16,12,20)] # legs

# sizes of the parts after being scaled (scale factor = 48)
newSizes = [(384,384), (1536,384), (384,384), # head
            (384,192), (1152,576), (384,192), # body
            (192,192), (768,576), (192,192), # arms
            (192,192), (768,576), (192,192)] # legs

# locations of the parts in the finished, printable image
printCoords = [(450,75), (66,459), (450,843), # head
               (600,1350), (408,1542), (600,2118), # body
               (1930,140), (1738,332), (1930,908), # arm
               (300,2275), (108,2467), (300,3043), # leg
               (2040,1170), (1656,1362), (2040,1938), # reversed arm
               (1600,2275), (1216,2467), (1600,3043)] # reversed leg

# print usage if the number of arguments is wrong
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
draw = ImageDraw.Draw(printable)

draw.text((120,180), "Head", fill=(0,0,0))
draw.text((180,1400), "Body", fill=(0,0,0))
draw.text((1650,180), "Arms", fill=(0,0,0))
draw.text((100,2300), "Legs", fill=(0,0,0))

#
# Cut out sections of the skin file, scale them, and paste them into our image
#

for i in range(12):
	printable.paste(skin.crop(skinCoords[i]).resize(newSizes[i]), printCoords[i])

for i in range(12, 18):
	printable.paste(skin.crop(skinCoords[i-6]).resize(newSizes[i-6]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[i])

#
# Save the image
#
printable.save(sys.argv[2])
