# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

n = set(input().split())
m = int(input())
count = 0

for x in range(m):
    y = set(input().split())
    if (n.issuperset(y)):
        count += 1
        
print(count == m)


# Solutions from site 1/2
s = set(input().split())
ans = True
for i in range(int(input())):
    t = set(input().split())
    if (s > t) == False:
        ans = False
        break
print(ans)        


# Solutions from site 2/2
def isstrictsuperset(a,b):
    # true if a is a strict superset of b
    return b.issubset(a) and not(a.issubset(b))

a = set(int(x) for x in input().split(' '))
n = int(input())
res = True

for _ in range(n):
    b = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(a,b)
    
print(res)
