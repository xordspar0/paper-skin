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
               (1930,140), (1738,332), (1930,908), # arms
               (2040,1170), (1656,1362), (2040,1938),
               (300,2275), (108,2467), (300,3043), # legs
               (1600,2275), (1216,2467), (1600,3043)]

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

printable.paste(skin.crop(skinCoords[0]).resize(newSizes[0]), printCoords[0])
printable.paste(skin.crop(skinCoords[1]).resize(newSizes[1]), printCoords[1])
printable.paste(skin.crop(skinCoords[2]).resize(newSizes[2]), printCoords[2])
printable.paste(skin.crop(skinCoords[3]).resize(newSizes[3]), printCoords[3])
printable.paste(skin.crop(skinCoords[4]).resize(newSizes[4]), printCoords[4])
printable.paste(skin.crop(skinCoords[5]).resize(newSizes[5]), printCoords[5])
printable.paste(skin.crop(skinCoords[6]).resize(newSizes[6]), printCoords[6])
printable.paste(skin.crop(skinCoords[7]).resize(newSizes[7]), printCoords[7])
printable.paste(skin.crop(skinCoords[8]).resize(newSizes[8]), printCoords[8])
printable.paste(skin.crop(skinCoords[6]).resize(newSizes[6]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[9])
printable.paste(skin.crop(skinCoords[7]).resize(newSizes[7]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[10])
printable.paste(skin.crop(skinCoords[8]).resize(newSizes[8]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[11])
printable.paste(skin.crop(skinCoords[9]).resize(newSizes[9]), printCoords[12])
printable.paste(skin.crop(skinCoords[10]).resize(newSizes[10]), printCoords[13])
printable.paste(skin.crop(skinCoords[11]).resize(newSizes[11]), printCoords[14])
printable.paste(skin.crop(skinCoords[9]).resize(newSizes[9]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[15])
printable.paste(skin.crop(skinCoords[10]).resize(newSizes[10]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[16])
printable.paste(skin.crop(skinCoords[11]).resize(newSizes[11]).transpose(Image.FLIP_LEFT_RIGHT), printCoords[17])

#
# Save the image
#
printable.save(sys.argv[2])
