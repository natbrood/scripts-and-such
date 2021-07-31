#!/bin/bash

GREEN='\033[0;92m'
RED='\033[0;91m'
CLEAR='\033[0m'


if [ -z "$1" ] || [ ! -e "$1" ]
	then
		echo -e "Usage: unzip_matryoshka [file]\n"
		exit 1
	else
		outputfolder=`mkdir unzip_output`
		filename=$1
		password=`unzip -l $filename | head -4 | tail -1| cut -d" " -f10 | tr -d '.zip'`
		
		echo -e "Unpacking $filename with password: $password" 
		unpack=`unzip -P $password $filename -d unzip_output`
		echo $unpack
		echo -e "${GREEN}Succsessful${CLEAR}: $filename had been unpacked\n"
		inflating=`echo $unpack | cut -d" " -f3`
		count=1
		echo -e "Unpacked $count time!\n\n"

		
	while :
	do
		if [[ $inflating == *"inflating"* ]]
		then
			count=$(( $count + 1 ))
			filename="$password.zip"
			password=`unzip -l unzip_output/$filename | head -4 | tail -1| cut -d" " -f10 | tr -d '.zip'`
			
			echo -e "Unpacking $filename with password: $password" 
			unpack=`unzip -P $password unzip_output/$filename -d unzip_output`
			echo $unpack
			echo -e "${GREEN}Succsessful${CLEAR}: $filename had been unpacked\n"
			inflating=`echo $unpack | cut -d" " -f3`
			echo -e "Unpacked $count times!\n\n"
			
		else
			echo -e "${RED}Error${CLEAR}: Password incorrect or reached the end.\n"
			break

		fi
	done
fi
