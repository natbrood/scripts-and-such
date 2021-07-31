# https://pythonprinciples.com/challenges/Flatten-a-list/

# Version 1
def flatten(listing):
    result = []
    for x,y in listing:
        result.append(x)
        result.append(y)
    print(result)


flatten([[1, 2], [3, 4]])   


# Version 2
def flatten(listing):
    return sum(listing, [])

flatten([[1, 2], [3, 4]])    


# Solution from site
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]