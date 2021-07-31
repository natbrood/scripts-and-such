# https://pythonprinciples.com/challenges/Divisible-by-3/

def div_3(number):
    return (number/3).is_integer()

div_3(6)


# Solution from site
def div_3(n):
    return n % 3 == 0