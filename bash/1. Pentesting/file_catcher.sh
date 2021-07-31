#!/bin/bash

folder="SSH/"
echo "I will copy the file that gets placed in "$folder

while : 
do
	lscommand=`ls $folder`
	#sleep 1
	output=$lscommand
	echo -n $lscommand > /dev/null;

	if [ -n "$lscommand" ]
	then
		echo "This is the file I found: "$lscommand
		echo`cp SSH/$output .`
		break
	fi

done
