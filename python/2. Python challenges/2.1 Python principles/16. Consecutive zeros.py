# https://pythonprinciples.com/challenges/Consecutive-zeros/

def consecutive_zeros(string):
    #print('00' in string)
    #print(['0' in a == b for a,b in zip(string, string)])
    return len(max(string.split('1')))
consecutive_zeros("1001101000110")


# Solution from site
# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
