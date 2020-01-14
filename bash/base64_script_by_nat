#!/bin/bash
echo -e "Required: The 'base64' application\n"

echo "This script will Base64 a set amount of times."

read -p "Name the input file: " input
read -p "Name the amount of times the script should run: " amount
echo -e "\n"


echo "Encrypt or Decrypt?"
echo -e "Select an option:\n"

echo "  1)  Encrypt"
echo -e "  2)  Decrypt\n"

read n
echo -e "\n"

echo -e "Output:\n\n"


case $n in
  1) 	echo ""
	cat $input | tr -d ' ' > tmpfile

	for i in $(seq 1 $amount) ; do

		echo "Encrypt:" $i

		output=`cat tmpfile | base64`
		sleep 0.2
		echo $output | tr -d ' ' > tmpfile
		cat tmpfile

		echo -e "\n"
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

		echo -e "\n"
	done
	mv tmpfile decrypted.b64

	echo "Decryption complete!"
	echo "Outputfile:" `pwd`"/decrypted.b64"
;;

  *) echo "invalid option";;
esac
