#!/bin/bash
echo "Required: The 'base64' application"
echo ""

echo "This script will Base64 a set amount of times."
echo ""
read -p "Name the input file: " input
echo ""

read -p "Name the amount of times the script should run: " amount
echo ""
echo ""


echo "Encrypt or Decrypt?"
echo "Select an option:"
echo ""
echo "  1)  Encrypt"
echo "  2)  Decrypt"
echo ""
read n
echo ""
echo ""


echo "================================================================="
echo ""
echo "Output:"
echo ""
echo ""


case $n in
  1) 	echo ""
	cat $input | tr -d ' ' > tmpfile

	for i in $(seq 1 $amount) ; do

		echo "Encrypt:" $i

		output=`cat tmpfile | base64`
		sleep 0.2
		echo $output | tr -d ' ' > tmpfile
		cat tmpfile

		echo ""
		echo ""
	done
	mv tmpfile encrypted.b64

	echo "Encryption complete!"
	echo "Outputfile:" `pwd`"/encrypted.b64"
;;

  2) 	echo ""
	cat $input | tr -d ' ' > tmpfile

	for i in $(seq 1 $amount) ; do

		echo "Decrypt:" $i

		output=`cat tmpfile | base64 -d`
		sleep 0.2
		echo $output | tr -d ' ' > tmpfile
		cat tmpfile

		echo ""
		echo ""
	done
	mv tmpfile decrypted.b64

	echo "Decryption complete!"
	echo "Outputfile:" `pwd`"/decrypted.b64"
;;

  *) echo "Invalid option, try again";;
esac
