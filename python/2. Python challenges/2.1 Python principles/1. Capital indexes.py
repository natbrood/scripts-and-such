# https://pythonprinciples.com/challenges/Capital-indexes/

def capital_indexes(string):
    dalist = []
    for count,value in enumerate(string):
        if (value.isupper()) == True:
            dalist.append(count)
    return dalist
        
capital_indexes("HeLlO")


# Solution from site

# naive solution
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.
