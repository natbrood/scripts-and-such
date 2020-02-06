import sys
import argparse
import time
from colorama import Style

def encrypt(text, key): # calls function: encrypt with the 
    keylen = len(key) # looks up the length of the key
    keyPos = 0 # creating the interger keyPos
    encrypted = "" # creating the string 'encrypted'

    for x in text: # for loop, for every character in "text"
        keyChr = key[keyPos] # select keyPos 0 (Chartacter number 0, 0 = first) 
        newChr = ord(x) # translate the character to the unicode number
        newChr = chr((newChr + ord(keyChr)) % 255) # unicode character = (unicode number of key + unicode of key position) / 255
        encrypted += newChr # collect all the encrypted characters
        keyPos += 1 # keyPos +1
        keyPos = keyPos % keylen # keyposition / lenght of the key = that what remains of this equation
    return encrypted

def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted

parser = argparse.ArgumentParser(description='Encrypt, Decrypt the encryption algorithm')

parser.add_argument('-i',
                    metavar='Input',
                    type=str,
                    help='The file to encrypt/decrypt',
                    required=False)

parser.add_argument('-o',
                    metavar='Output',
                    type=str,
                    help='Where to output the encrypted/decrypted file',
                    required=False)

parser.add_argument('-k',
                    metavar='Key',
                    type=str,
                    help='Key to use',
                    required=False)

parser.add_argument('--dict',
                    metavar='Wordlist',
                    type=str,
                    help='Dictionary to use (Bruteforce mode only) \nHowever, this password cannot contain just spaces on its own. The script will crash.',
                    required=False)

parser.add_argument('-d', action='store_true', help='Decrypt mode')
parser.add_argument('-b', action='store_true', help='Bruteforce mode')

args = parser.parse_args()

banner = '\n\n\033[1;34;40m dP"Yb  88""Yb .dP"8   dP""8b 88   88 88""Yb    db\n'
banner+= '\033[1;34;40mdP   Yb 88__dP `Ybo   dP   `" 88   88 88__dP   dPYb\n'
banner+= '\033[1;34;40mYb   dP 88""Yb   `Yb  Yb      Y8   8P 88"Yb   dP__Yb \n'
banner+= '\033[1;34;40m Brood  88oodP 8bodP   YboodP `YbodP  88  Yb dP""""Yb\n'
print(banner)
print(Style.RESET_ALL)
if args.i == None:
    print("Missing Input File")
elif args.o == None:
    print("Missing args")

else:
    # Decrypt mode
    if args.d:
        print("Opening file {0}...".format(args.i))
        with open(args.i, 'r', encoding='UTF-8') as f:
            data = f.read()

        print("Decrypting...")
        decrypted = decrypt(data, args.k)

        print("Writing to {0}...".format(args.o))
        with open(args.o, 'w', encoding='UTF-8') as f:
            f.write(decrypted)

    # Brute force mode
    elif args.b:
        print("Bruteforcing: ")
        passwdfile = args.dict
        passwdfile = open(passwdfile, "r")
        args.k = ""

        for args.k in passwdfile:
            args.k = args.k.rstrip()
            print("\033[0;37;40mCurrently trying key: " + args.k)
            #print("###" + args.k + "###")

            with open(args.i, 'r', encoding='UTF-8') as f:
                data = f.read()

            decrypted = decrypt(data, args.k)
            #time.sleep(0.0001)

            # Wanted result check
            if "Encrypting this file" in decrypted:
                print("\n\n\033[1;32;40mFOUND THE PASSWORD")
                print(Style.RESET_ALL)
                print("\nThe password is: \033[1;31;40m" + args.k)
                print(Style.RESET_ALL)
                print("Writing outcome of the decrypted input to: {0}\n".format(args.o))
                with open(args.o, 'w', encoding='UTF-8') as f:
                    f.write(decrypted)
                sys.exit()

            else:
                continue


    # No mode (encrypt)
    else:
        print("Opening file {0}...".format(args.i))
        with open(args.i, 'r', encoding='UTF-8') as f:
            data = f.read()

        print("Encrypting...")
        encrypted = encrypt(data, args.k)

        print("Writing to {0}...".format(args.o))
        with open(args.o, 'w', encoding='UTF-8') as f:
            f.write(encrypted)
