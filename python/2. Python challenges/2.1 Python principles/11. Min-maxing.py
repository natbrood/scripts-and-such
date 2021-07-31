# https://pythonprinciples.com/challenges/Minmaxing/

def largest_difference(listing):
    return max(listing)-min(listing)
    
largest_difference([-100, 100])


# Solution from site
# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
