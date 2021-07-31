# https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem


read character

if [[ $character = "y" || $character = "Y" ]]; then
    echo "YES"
elif [[ $character = "n" || $character = "N" ]]; then
    echo "NO"
fi
