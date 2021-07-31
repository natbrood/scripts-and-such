# https://pythonprinciples.com/challenges/Counting-syllables/

def count(string):
    return len(string.split("-"))
        
count("met-a-phor")


# Solution from site
# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))
