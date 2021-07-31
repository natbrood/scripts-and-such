# https://pythonprinciples.com/challenges/Writing-short-code/

def convert(listing):
    return [str(a) for a in listing]
    
#convert([1, 2, 3])

# Solution from site
# using a list comprehension
def convert(ns):
    return [str(n) for n in ns]

# using map
def convert(ns):
    return list(map(str, ns))
