# https://pythonprinciples.com/challenges/Custom-zip/

def zap(a,b):
    return [(a[i], b[i]) for i in range(0, len(a))]
       
zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
    )


# Solution from site
# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result

# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]
