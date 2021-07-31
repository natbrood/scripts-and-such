# https://pythonprinciples.com/challenges/Type-check/

def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False

only_ints(1,2)


# Solution from site
def only_ints(a, b):
    return type(a) == int and type(b) == int
