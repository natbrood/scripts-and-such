# https://www.hackerrank.com/challenges/bash-tutorials---looping-with-numbers/problem

i=0

while [ $i -lt 50 ]
do
    ((i++))
    echo $i
done

