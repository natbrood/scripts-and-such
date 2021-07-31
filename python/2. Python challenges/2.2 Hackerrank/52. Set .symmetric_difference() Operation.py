# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


engN,engS,frN,frS = input(),set(input().split()),input(),set(input().split())
print(len(engS.symmetric_difference(frS)))


# Solutions from site
num1 = int(input())
setA = set(map(int, input().split()))
num2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.symmetric_difference(setB)))
