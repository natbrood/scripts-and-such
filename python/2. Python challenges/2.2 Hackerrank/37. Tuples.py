# https://www.hackerrank.com/challenges/python-tuples/problem


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    
    print(hash(integer_list))


# Solutions from site
N = int(input())
T = tuple(int(x) for x in input().split())
print(hash(T))
