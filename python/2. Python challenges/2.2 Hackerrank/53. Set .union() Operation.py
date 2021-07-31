# https://www.hackerrank.com/challenges/py-set-union/problem

engN,engS,frN,frS = input(),set(input().split()),input(),set(input().split())
print(len(engS.union(frS)))


# Solutions from site
num1 = int(input())
setA = set(map(int, input().split()))
num2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.union(setB)))
