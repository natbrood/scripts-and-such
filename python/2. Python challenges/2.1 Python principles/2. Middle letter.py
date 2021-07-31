# https://pythonprinciples.com/challenges/Middle-letter/

# Version 1
def mid(num):
    if len(num) % 2 == 0:
        print("")
    else:
        midnum = num[int(len(num)/2)]
        print(midnum)
mid("abc")

# Version 2
def mid(num):
    if len(num) & 1 == 1:
        midnum = num[int(len(num)/2)]
        return midnum
    else:
        return ""
mid("abc")

# Solution from site
# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
