# https://pythonprinciples.com/challenges/All-equal/

def all_equal(listing):
    return all([a == b for a, b in zip(listing,listing[1:])])
    
all_equal([1,2,3])


# Solution from site
# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)