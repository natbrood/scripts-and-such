# https://pythonprinciples.com/challenges/Solution-validation/

dictionary1 = {
    "missing def" : ["def"],
    "missing :" : [":"],
    "missing paren" : ["(",")"]
    }
dictionary2 = {
    "missing indent" : ["    "],
    "wrong name" : ["validate"],
    "missing return" : ["return"]
    }

def validate(code):
    for error in dictionary1:
        for key in dictionary1[error]:
            if key not in code:
                return error
                #return
    if "("+")" in code:
        return "missing param"
    for error in dictionary2:
        for key in dictionary2[error]:
            if key not in code:
                return error
                #return
    return True
print(validate('def     validate(x):\n return True'))


# Solution from site
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

# https://stackoverflow.com/questions/17340922/how-to-search-if-dictionary-value-contains-certain-string-with-python
