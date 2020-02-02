#!/usr/bin/env python
#
# By Nathan Brood
# Note: this script gets stuck at 837.zip
#
# Import the PIL library - pip3 install Pillow

from zipfile import ZipFile
from PIL import Image
import subprocess
import time
import sys

if len(sys.argv) == 1:
    sys.exit("Usage: image_morse2unzip <zipfile> <image with morse>")
elif len(sys.argv) == 2:
    sys.exit("Usage: image_morse2unzip <zipfile> <image with morse>")
else:
    morse_zip = sys.argv[1]
    imagefile = sys.argv[2]

# MORSE CODE DICT
Pix2Morse_upper = {
    'A': '-█-███-------------------',
    'B': '-███-█-█-█---------------',
    'C': '-███-█-███-█-------------',
    'D': '-███-█-█-----------------',
    'E': '-█-----------------------',
    'F': '-█-█-███-█---------------',
    'G': '-███-███-█---------------',
    'H': '-█-█-█-█-----------------',
    'I': '-█-█---------------------',
    'J': '-█-███-███-███-----------',
    'K': '-███-█-███---------------',
    'L': '-█-███-█-█---------------',
    'M': '-███-███-----------------',
    'N': '-███-█-------------------',
    'O': '-███-███-███-------------',
    'P': '-█-███-███-█-------------',
    'Q': '-███-███-█-███-----------',
    'R': '-█-███-█-----------------',
    'S': '-█-█-█-------------------',
    'T': '-███---------------------',
    'U': '-█-█-███-----------------',
    'V': '-█-█-█-███---------------',
    'W': '-█-███-███---------------',
    'X': '-███-█-█-███-------------',
    'Y': '-███-█-███-███-----------',
    'Z': '-███-███-█-█-------------',
    '1': '-█-███-███-███-███-------',
    '2': '-█-█-███-███-███---------',
    '3': '-█-█-█-███-███-----------',
    '4': '-█-█-█-█-███-------------',
    '5': '-█-█-█-█-█---------------',
    '6': '-███-█-█-█-█-------------',
    '7': '-███-███-█-█-█-----------',
    '8': '-███-███-███-█-█---------',
    '9': '-███-███-███-███-█-------',
    '0': '-███-███-███-███-███-----',
    '': '-------------------------'
    }


Pix2Morse_lower = {
    'a': '-█-███-------------------',
    'b': '-███-█-█-█---------------',
    'c': '-███-█-███-█-------------',
    'd': '-███-█-█-----------------',
    'e': '-█-----------------------',
    'f': '-█-█-███-█---------------',
    'g': '-███-███-█---------------',
    'h': '-█-█-█-█-----------------',
    'i': '-█-█---------------------',
    'j': '-█-███-███-███-----------',
    'k': '-███-█-███---------------',
    'l': '-█-███-█-█---------------',
    'm': '-███-███-----------------',
    'n': '-███-█-------------------',
    'o': '-███-███-███-------------',
    'p': '-█-███-███-█-------------',
    'q': '-███-███-█-███-----------',
    'r': '-█-███-█-----------------',
    's': '-█-█-█-------------------',
    't': '-███---------------------',
    'u': '-█-█-███-----------------',
    'v': '-█-█-█-███---------------',
    'w': '-█-███-███---------------',
    'x': '-███-█-█-███-------------',
    'y': '-███-█-███-███-----------',
    'z': '-███-███-█-█-------------',
    '1': '-█-███-███-███-███-------',
    '2': '-█-█-███-███-███---------',
    '3': '-█-█-█-███-███-----------',
    '4': '-█-█-█-█-███-------------',
    '5': '-█-█-█-█-█---------------',
    '6': '-███-█-█-█-█-------------',
    '7': '-███-███-█-█-█-----------',
    '8': '-███-███-███-█-█---------',
    '9': '-███-███-███-███-█-------',
    '0': '-███-███-███-███-███-----',
    '': '-------------------------'
    }


def decrypt_up(message_up):

    # extra space added at the end to access the
    # last morse code
    message_up += ' '

    decipher_up = ''
    citext_up = ''
    for letter_up in message_up:

        # checks for space
        if (letter_up != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext_up += letter_up

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher_up += ' '

            else:
                # accessing the keys using their values (reverse of encryption)
                decipher_up += list(Pix2Morse_upper.keys())[list(
                    Pix2Morse_upper.values()).index(citext_up)]
                citext_up = ''

            return decipher_up

def decrypt_lo(message_lo):

    # extra space added at the end to access the
    # last morse code
    message_lo += ' '

    decipher_lo = ''
    citext_lo = ''
    for letter_lo in message_lo:

        # checks for space
        if (letter_lo != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext_lo += letter_lo

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher_lo += ' '

            else:
                # accessing the keys using their values (reverse of encryption)
                decipher_lo += list(Pix2Morse_lower.keys())[list(
                    Pix2Morse_lower.values()).index(citext_lo)]
                citext_lo = ''

            return decipher_lo

# Wat je kunt doen is het gebruiken van arguments ipv iets als een menu als dit
menu = """
Image_morse 2 unzip

Select one of the following:
1   : Challenge mode (works up to: 837.zip)
2   : Image2morse
3   : Exit

"""

print (menu)

ans = True
ans = input("Select your option:  ")
if ans == "1":
    # Unzip the first zip (the one w)

    # Get image and overwrite log
    im = Image.open(imagefile)
    # open('log/morse2unzip.log', 'w')
    # logging = open('log/morse2unzip.log', 'a')

    # Set up initial values
    width = im.size[0]
    height = im.size[1]
    row = 1
    col = 1
    pix = 0
    rowdata = ""
    password_up = ""
    password_lo = ""

    # Get hex value of the first pixel
    r_bg, g_bg, b_bg = im.getpixel((col - 1, row - 1))
    r_bg_int = int(r_bg)
    pix_a = format(r_bg_int, '02x')
    g_bg_int = int(g_bg)
    pix_b = format(g_bg_int, '02x')
    b_bg_int = int(b_bg)
    pix_c = format(b_bg_int, '02x')
    firstpixel = pix_a + pix_b + pix_c
    print("\n" + imagefile)
    print(firstpixel)

    while row < height + 1:
        while col < width + 1:
            r, g, b = im.getpixel((col - 1, row - 1))
            # RGB to Hexadecimal
            r_int = int(r)
            reds = format(r_int, '02x')
            g_int = int(g)
            greens = format(g_int, '02x')
            b_int = int(b)
            blues = format(b_int, '02x')
            pixel = str(reds) + str(greens) + str(blues)
            # Hex to Morse
            if pixel == firstpixel:
                unicode = "-"
            else:
                unicode = "█"
            rowdata += str(unicode) + ""
            # rowdata += str(pixel) + ""
            col = col + 1
            pix = pix + 1

        # Morse translator
        message_up = rowdata
        message_lo = rowdata
        result_up = decrypt_up(message_up)
        result_lo = decrypt_lo(message_lo)
        password_up += decrypt_up(message_up)
        password_lo += decrypt_lo(message_lo)
        # print(result)
        print(rowdata)
        # logging.write(result)

        rowdata = ""
        row = row + 1
        col = 1

    # Unzip the file
    print("Unzipping " + morse_zip + " with password_up: " + password_up + "\n")
    command1 = "unzip -o -P" + password_up + " " + morse_zip + " -d unpack"
    process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output_zip = process1.communicate()[0]
    # print(output_zip)
    input_zip = str(output_zip)

    command2 = 'echo "' + input_zip + '" |tr -d "\n" | cut -d" " -f14 |tr -d "\n" |tr -d "\'"'
    process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output_filter = process2.communicate()[0]
    # print(output_filter)

    command3 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f5 |tr -d "\n" |tr -d "\'"'
    process3 = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE)
    output_unpacked = process3.communicate()[0]
    # print(output_unpacked)

    command4 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f10 |tr -d "\n" |tr -d "\'" '
    process4 = subprocess.Popen(command4, shell=True, stdout=subprocess.PIPE)
    output_unpacked_image = process4.communicate()[0]

    clean_filter = output_filter.decode()
    unpacked_zip = output_unpacked.decode()
    unpacked_image = output_unpacked_image.decode()
    print("clean_filter" + clean_filter)
    print("unpacked_image" + unpacked_image)
    print("unpacked_zip" + unpacked_zip)


    if clean_filter == "incorrect":
    	print("wrong password!")
    	print("Unzipping " + morse_zip + " with password_lo: " + password_lo + "\n")
    	command1 = "unzip -o -P" + password_lo + " " + morse_zip + " -d unpack"
    	process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    	output_zip = process1.communicate()[0]
    	# print(output_zip)
    	input_zip = str(output_zip)

    	command2 = 'echo "' + input_zip + '" |tr -d "\n" | cut -d" " -f14 |tr -d "\n" |tr -d "\'"'
    	process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    	output_filter = process2.communicate()[0]
    	# print(output_filter)

    	command3 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f5 |tr -d "\n" |tr -d "\'"'
    	process3 = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE)
    	output_unpacked = process3.communicate()[0]
    	# print(output_unpacked)

    	command4 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f10 |tr -d "\n" |tr -d "\'" '
    	process4 = subprocess.Popen(command4, shell=True, stdout=subprocess.PIPE)
    	output_unpacked_image = process4.communicate()[0]

    	clean_filter = output_filter.decode()
    	unpacked_zip = output_unpacked.decode()
    	unpacked_image = output_unpacked_image.decode()
    	print("clean_filter" + clean_filter)
    	print("unpacked_image" + unpacked_image)
    	print("unpacked_zip" + unpacked_zip)

    	if clean_filter == "incorrect":
    		print("Wrong again")
    		sys.exit("Stopping script")
    	else:
    		password_lo_match = "true"
    else:
    	password_lo_match = "true"

    while password_lo_match == "true":
        # Set up initial values
        print("Correct password!")
        morse_zip = unpacked_zip
        im = Image.open(unpacked_image)
        width = im.size[0]
        height = im.size[1]
        row = 1
        col = 1
        pix = 0
        rowdata = ""
        password_up = ""
        password_lo = ""

        # Get hex value of the first pixel
        r_bg, g_bg, b_bg = im.getpixel((col - 1, row - 1))
        r_bg_int = int(r_bg)
        pix_a = format(r_bg_int, '02x')
        g_bg_int = int(g_bg)
        pix_b = format(g_bg_int, '02x')
        b_bg_int = int(b_bg)
        pix_c = format(b_bg_int, '02x')
        firstpixel = pix_a + pix_b + pix_c
        print("\n" + unpacked_zip)
        print(firstpixel)

        #time.sleep(0.2)

        while row < height + 1:
            while col < width + 1:
                r, g, b = im.getpixel((col - 1, row - 1))
                # RGB to Hexadecimal
                r_int = int(r)
                reds = format(r_int, '02x')
                g_int = int(g)
                greens = format(g_int, '02x')
                b_int = int(b)
                blues = format(b_int, '02x')
                pixel = str(reds) + str(greens) + str(blues)
                # Hex to Morse
                if pixel == firstpixel:
                    unicode = "-"
                else:
                    unicode = "█"
                rowdata += str(unicode) + ""
                col = col + 1
                pix = pix + 1
            # Morse translator
            message_up = rowdata
            message_lo = rowdata
            result_up = decrypt_up(message_up)
            result_lo = decrypt_lo(message_lo)
            password_up += decrypt_up(message_up)
            password_lo += decrypt_lo(message_lo)
            print(rowdata)

            rowdata = ""
            row = row + 1
            col = 1

        # Unzip the file
        print("Unzipping " + morse_zip + " with password_up: " + password_up + "\n")
        command1 = "unzip -o -P" + password_up + " " + morse_zip + " -d unpack"
        process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_zip = process1.communicate()[0]
        # print(output_zip)
        input_zip = str(output_zip)

        command2 = 'echo "' + input_zip + '" |tr -d "\n" | cut -d" " -f14 |tr -d "\n" |tr -d "\'"'
        process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_filter = process2.communicate()[0]
        # print(output_filter)

        command3 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f5 |tr -d "\n" |tr -d "\'"'
        process3 = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE)
        output_unpacked = process3.communicate()[0]
        # print(output_unpacked)

        command4 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f10 |tr -d "\n" |tr -d "\'"'
        process4 = subprocess.Popen(command4, shell=True, stdout=subprocess.PIPE)
        output_unpacked_image = process4.communicate()[0]
        #print(output_unpacked_image)

        clean_filter = output_filter.decode()
        unpacked_zip = output_unpacked.decode()
        # unpacked_image = output_unpacked_image.decode()
        unpacked_image = "unpack/flag/pwd.png"
        # print(clean_filter)
        #print(unpacked_image)
        # print(unpacked_zip)
        #time.sleep(0.2)
        if clean_filter == "incorrect":
        	print("wrong password!")
        	print("Unzipping " + morse_zip + " with password_lo: " + password_lo + "\n")
        	command1 = "unzip -o -P" + password_lo + " " + morse_zip + " -d unpack"
        	process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        	output_zip = process1.communicate()[0]
        	# print(output_zip)
        	input_zip = str(output_zip)

        	command2 = 'echo "' + input_zip + '" |tr -d "\n" | cut -d" " -f14 |tr -d "\n" |tr -d "\'"'
        	process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        	output_filter = process2.communicate()[0]
        	# print(output_filter)

        	command3 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f5 |tr -d "\n" |tr -d "\'"'
        	process3 = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE)
        	output_unpacked = process3.communicate()[0]
        	# print(output_unpacked)

        	command4 = 'echo -n "' + input_zip + '"|tr -d "\n" | cut -d" " -f10 |tr -d "\n" |tr -d "\'" '
        	process4 = subprocess.Popen(command4, shell=True, stdout=subprocess.PIPE)
        	output_unpacked_image = process4.communicate()[0]

        	clean_filter = output_filter.decode()
        	unpacked_zip = output_unpacked.decode()
        	unpacked_image = output_unpacked_image.decode()
        	print("clean_filter" + clean_filter)
        	#print("unpacked_image" + unpacked_image)
        	unpacked_image = "unpack/flag/pwd.png"
        	print("unpacked_zip" + unpacked_zip)

        	if clean_filter == "incorrect":
        		print("Wrong again")
        		sys.exit("Stopping script")
        	else:
        		print("Correct password!")
        		password_lo_match = "true"
        else:
        	print("Correct password!")
        	password_lo_match = "true"
        print("Correct password!")
        time.sleep()



    print("\nDone")


elif ans == "2":
    # Get image and overwrite log
    im = Image.open(imagefile)
    open('log/morse2text.log', 'w')
    logging = open('log/morse2text.log', 'a')

    # Set up initial values
    width = im.size[0]
    height = im.size[1]
    row = 1
    col = 1
    pix = 0
    rowdata = ""
    password = ""

    # Get hex value of the first pixel
    r_bg, g_bg, b_bg = im.getpixel((col - 1, row - 1))
    r_bg_int = int(r_bg)
    pix_a = format(r_bg_int, '02x')
    g_bg_int = int(g_bg)
    pix_b = format(g_bg_int, '02x')
    b_bg_int = int(b_bg)
    pix_c = format(b_bg_int, '02x')
    firstpixel = pix_a + pix_b + pix_c
    print("\n" + firstpixel)

    while row < height + 1:
        while col < width + 1:
            r, g, b = im.getpixel((col - 1, row - 1))
            # RGB to Hexadecimal
            r_int = int(r)
            reds = format(r_int, '02x')
            g_int = int(g)
            greens = format(g_int, '02x')
            b_int = int(b)
            blues = format(b_int, '02x')
            pixel = str(reds) + str(greens) + str(blues)
            # Hex to Morse
            if pixel == firstpixel:
                unicode = "-"
            else:
                unicode = "█"
            rowdata += str(unicode) + ""
            col = col + 1
            pix = pix + 1

        # Morse translator
        message = rowdata
        result = decrypt(message)
        password += decrypt(message)
        print(result)
        logging.write(result)

        rowdata = ""
        row = row + 1
        col = 1


elif ans == "3":
    sys.exit("")
