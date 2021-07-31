# https://www.hackerrank.com/challenges/py-check-subset/problem


n = int(input())

def checker():
    aNR = input()
    a = set(input().split(' '))
    bNR = input()
    b = set(input().split(' '))
    print(a.issubset(b))

for n in range(n):
    checker()


# Solutions from site 1/2
for i in range(int(input())): #More than 4 lines will result in 0 score. Do not leave a blank line also. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A.issubset(B))


# Solutions from site 2/2
for _ in range(int(input())):
    a,s,d,f = input(), set(map(int, (input().split()))), input(), set(map(int, (input().split())))
    print(set(s).issubset(f))

# https://www.w3schools.com/python/ref_set_issubset.asp
	
# https://programs.programmingoneonone.com/2021/02/hackerrank-input-solution-python.html