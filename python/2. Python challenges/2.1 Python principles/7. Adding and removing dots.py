# https://pythonprinciples.com/challenges/Adding-and-removing-dots/

def add_dots(string1):
    dotted = ""
    for x in string1:
        dotted += x + "."
    return dotted[:-1]

def remove_dots(string2):
    return string2.replace('.','')

add_dots("abc")
remove_dots("t.e.s.t.")


# Solution from site
# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
