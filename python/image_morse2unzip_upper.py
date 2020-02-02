#!/usr/bin/env python
#
# By Nathan Brood
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
Pix2Morse = {
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


def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '

            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(Pix2Morse.keys())[list(
                    Pix2Morse.values()).index(citext)]
                citext = ''

            return decipher

# Wat je kunt doen is het gebruiken van arguments ipv iets als een menu als dit
menu = """
Image_morse 2 unzip

Select one of the following:
1   : Challenge mode (works up to: 986.zip)
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
            # rowdata += str(pixel) + ""
            col = col + 1
            pix = pix + 1

        # Morse translator
        message = rowdata
        result = decrypt(message)
        password += decrypt(message)
        # print(result)
        print(rowdata)
        # logging.write(result)

        rowdata = ""
        row = row + 1
        col = 1

    # Unzip the file
    print("Unzipping " + morse_zip + " with password: " + password + "\n")
    command1 = "unzip -o -P" + password + " " + morse_zip + " -d unpack"
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

    #sys.exit("fullstop")
    # LOOP

    while clean_filter != "incorrect":
        # Set up initial values
        morse_zip = unpacked_zip
        im = Image.open(unpacked_image)
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
            message = rowdata
            result = decrypt(message)
            password += decrypt(message)
            print(rowdata)

            rowdata = ""
            row = row + 1
            col = 1

        # Unzip the file
        print("Unzipping " + morse_zip + " with password: " + password + "\n")
        command1 = "unzip -o -P" + password + " " + morse_zip + " -d unpack"
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
