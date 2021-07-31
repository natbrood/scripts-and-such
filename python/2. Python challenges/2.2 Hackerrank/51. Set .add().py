# https://www.hackerrank.com/challenges/py-set-add/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
output = {input()}

for x in range(n-1):
    output.add(input())
print(len(output))


# Solutions from site
s = set()
for i in range(int(input())):
    s.add(input())
print(len(s))    
    
