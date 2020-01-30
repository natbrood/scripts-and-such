# Python script to display all pixels RGB values
# from an image and output them a row at a time
#
# Credit to original creator: Joh Witt (https://www.jonwitts.co.uk/archives/839#)
#
# Altered by Nathan Brood
#
# Import the PIL library - pip3 install Pillow

from PIL import Image
import sys

if len(sys.argv) == 1:
    sys.exit("Error missing filename: rgb2text <filename>")
else:
    filename = sys.argv[1]

ans=True
while ans:
    print ("""
    RGB Pixel values to text converter"
    

    Select one of the following:

    1        : Raw, only separated by a single space and new line per row of pixels"
    2        : Basic, like raw but with an extra line in between rows"
    3        : Pretty, numbers separated and in brackets combined with numbered rows
    4        : Exit
    
    """)
    ans=raw_input("Select your option:  ") 
    if ans=="1": 
	im = Image.open(filename)
	rgb_im = im.convert('RGB')
	width = rgb_im.size[0]
	height = rgb_im.size[1]
	row = 1
	col = 1
	pix = 0
	rowdata = ""
	while row < height + 1:
	    while col < width + 1:
		r, g, b = rgb_im.getpixel((col - 1, row - 1))
		rowdata += "" + str(r) + "," + str(g) + "," + str(b) + " "
		col = col + 1
		pix = pix + 1
	    print(rowdata)
	    rowdata = ""
	    row = row + 1
	    col = 1
	print("")
	break


    elif ans=="2":
	im = Image.open(filename)
	rgb_im = im.convert('RGB')
	width = rgb_im.size[0]
	height = rgb_im.size[1]
	row = 1
	col = 1
	pix = 0
	rowdata = ""
	while row < height + 1:
	    print("")
	    while col < width + 1:
		r, g, b = rgb_im.getpixel((col - 1, row - 1))
		rowdata += "" + str(r) + "," + str(g) + "," + str(b) + " "
		col = col + 1
		pix = pix + 1
	    print(rowdata)
	    rowdata = ""
	    row = row + 1
	    col = 1
	print("")
	break


    elif ans=="3":
	# Open our image
	im = Image.open(filename)
	 
	# Convert our image to RGB
	rgb_im = im.convert('RGB')
	 
	# Use the .size object to retrieve a tuple contain (width,height) of the image
	# and assign them to width and height variables
	width = rgb_im.size[0]
	height = rgb_im.size[1]
	 
	# set some counters for current row and column and total pixels
	row = 1
	col = 1
	pix = 0
	 
	# create an empty output row
	rowdata = ""
	 
	# loop through each pixel in each row outputting RGB value as we go...
	# all the plus and minus ones are to deal with the .getpixel class being
	# zero indexed and we want the output to start at pixel 1,1 not 0,0!
	while row < height + 1:
	    print("")
	    print("Row number: " + str(row))
	    while col < width + 1:
		# get the RGB values from the current pixel
		r, g, b = rgb_im.getpixel((col - 1, row - 1))
		# append the RGB values to the rowdata variable as (R, G, B)
		rowdata += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
		# increment the column count
		col = col + 1
		# increment the pixel count
		pix = pix + 1
	    # print out all RGB values for the row
	    print(rowdata)
	    # clear out rowdata variable
	    rowdata = ""
	    # increment the row...
	    row = row + 1
	    # reset the column count
	    col = 1
	 
	# output for proof!
	print("")
	print("Width = " + str(width) + " pixels")
	print("Height = " + str(height) + " pixels")
	print("Total Pixels = " + str(pix) + ".")
	break
    elif ans !="":
      sys.exit("") 



