# https://www.hackerrank.com/challenges/py-the-captains-room/problem


import collections
n = input()
m = input()
roomcount = dict(collections.Counter(m.split(' ')))

for x,y in roomcount.items():
    if y == 1:
        print(x)

#Too slow
#for roomnumber in rooms:
#    roomcounter = m.count(roomnumber)
#    if roomcounter == 1:
#        print(roomnumber)

#print(list(dict.fromkeys(rooms)))


# Solutions from site 1/2
k = int(input())
rooms = (int(x) for x in input().split(' '))
seen = {}

for i in rooms:
    if not i in seen:
        seen[i] = 1
    else:
        seen[i] += 1

for key, val in seen.items():
    if val != k:
        print(key)


# Solutions from site 2/2
n=int(input())
l=list(input().split())
from collections import defaultdict
d = defaultdict(int)
s=list(set(l))
for i in s:
    d[i]=0
for i in range(len(l)):
    d[l[i]]+=1 
for i in s:
    if d[i]==1:
        print(i)

# https://stackoverflow.com/questions/31807945/turning-a-collections-counter-into-dictionary
# https://thispointer.com/python-print-specific-key-value-pairs-of-dictionary/