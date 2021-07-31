# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    string = ""
    for x in s:
        if (x.isupper()):
            string += x.lower()
        elif (x.islower()):
            string += x.upper()
        else:
            string += x
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Solutions from site 1/2
string_input = input()
print(string_input.swapcase())


# Solutions from site 2/2
print(input().swapcase())
