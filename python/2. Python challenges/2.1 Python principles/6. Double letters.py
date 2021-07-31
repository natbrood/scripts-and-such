# https://pythonprinciples.com/challenges/Double-letters/

def double_letters(string):
    previous = ""
    for x in string:
        if x == previous:
            return True
            break
        else:
            previous = x
    return False
    
double_letters("Hello")


# Solution from site
# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
