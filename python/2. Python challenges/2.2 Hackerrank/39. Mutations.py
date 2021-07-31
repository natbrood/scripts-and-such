# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    listed = [char for char in string]
    listed[position] = character
    return ''.join(listed)

#can't edit what's below
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Solutions from site
s = input()
i, c = input().split()
i = int(i)
print(s[:i] + c + s[(i+1):])

# This dude actually split the line and reconstructed it. In a single line of code. Bruh