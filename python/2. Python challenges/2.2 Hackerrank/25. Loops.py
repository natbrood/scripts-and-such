# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)


# Solutions from site 1/2
n=int(raw_input())

for i in xrange(n):
    print i*i


# Solutions from site 2/2
n=int(input())
for i in range(n):
    print i**2
