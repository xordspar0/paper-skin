#! /usr/bin/env python3

import os, sys
from PIL import Image, ImageDraw, ImageFont

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

draw.rectangle([(449, 74), (834, 459)], (0, 0, 0))
draw.rectangle([(65, 458), (1602, 843)], (0, 0, 0))
draw.rectangle([(449, 842), (834, 1227)], (0, 0, 0))
draw.rectangle([(599, 1349), (984, 1542)], (0, 0, 0))
draw.rectangle([(407, 1541), (1560, 2118)], (0, 0, 0))
draw.rectangle([(599, 2117), (984, 2310)], (0, 0, 0))
draw.rectangle([(1929, 139), (2122, 332)], (0, 0, 0))
draw.rectangle([(1737, 331), (2506, 908)], (0, 0, 0))
draw.rectangle([(1929, 907), (2122, 1100)], (0, 0, 0))
draw.rectangle([(299, 2274), (492, 2467)], (0, 0, 0))
draw.rectangle([(107, 2466), (876, 3043)], (0, 0, 0))
draw.rectangle([(299, 3042), (492, 3235)], (0, 0, 0))
draw.rectangle([(2039, 1169), (2232, 1362)], (0, 0, 0))
draw.rectangle([(1655, 1361), (2424, 1938)], (0, 0, 0))
draw.rectangle([(2039, 1937), (2232, 2130)], (0, 0, 0))
draw.rectangle([(1599, 2274), (1792, 2467)], (0, 0, 0))
draw.rectangle([(1215, 2466), (1984, 3043)], (0, 0, 0))
draw.rectangle([(1599, 3042), (1792, 3235)], (0, 0, 0))


#
# Cut out sections of the skin file, scale them, and paste them into our image
#

# first the normal sections
for i in range(12):
	printable.paste(skin.crop(skinCoords[i]).resize(newSizes[i]),
	                printCoords[i])

# then the reversed sections
for i in range(12, 18):
	printable.paste(skin.crop(skinCoords[i-6]).resize(newSizes[i-6])
	                .transpose(Image.FLIP_LEFT_RIGHT), printCoords[i])

#
# Save the image
#
printable.save(sys.argv[2])
