# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    print(''.join([str(i+1) for i in range(n)]))


# Solutions from site 1/2
list(map(lambda i: print(i, end=''), [i for i in range(1, int(input()) + 1)]))


# Solutions from site 2/2
list(map(lambda x: print(x,end=''),list(range(1,1+int(input())))))
