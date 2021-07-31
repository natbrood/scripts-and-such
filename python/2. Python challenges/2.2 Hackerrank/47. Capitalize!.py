# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import re

# Complete the solve function below.
def solve(s):
    if re.search(" [0-9][a-z]",s):
        return ' '.join(x[0].upper()+x[1:] for x in s.split())
    else:
        return str.title(s)
    
    #return 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# Solutions from site 1/2
print ' '.join(word.capitalize() for word in raw_input().split(' '))


# Solutions from site 2/2
n = input().split(' ')
for i in n:
    print(i.capitalize(),end = " ")
