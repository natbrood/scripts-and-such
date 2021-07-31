# https://pythonprinciples.com/challenges/Counting-parameters/

def param_count(*variables):
    return len(variables)
    
print(param_count(2, 3, 4))


# Solution from site
def param_count(*args):
    return len(args)
