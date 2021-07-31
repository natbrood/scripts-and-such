# https://pythonprinciples.com/challenges/Thousands-separator/

def format_number(n):
    return '{:,}'.format(n)
    
format_number(12345678)


# Solution from site
# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)


# https://stackoverflow.com/questions/16670125/python-format-string-thousand-separator-with-spaces

# https://www.w3schools.com/python/ref_string_format.asp