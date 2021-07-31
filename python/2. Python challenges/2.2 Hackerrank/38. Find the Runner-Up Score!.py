# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(set(arr))[-2])
# [-2] at the end of a list = select the second to last


# Solutions from site 1/2
n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -6000, -6000
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)


# Solutions from site 2/2
n=int(input())
a=map(int,input().strip().split(" "))
a=list(a)
mx1=a[0]
mn=a[0]
for i in a:
    if(i>mx1):
        mx1=i
    if(i<mn):
        mn=i
mx2=mn
for i in a :
    if(i>mx2 and i<mx1):
        mx2=i
print(mx2)
