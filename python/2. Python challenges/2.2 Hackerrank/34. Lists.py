# https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input())
    list = []
    
    for x in range(N):
        y = input().split()
        if "insert" in y:
            list.insert(int(y[1]),int(y[2]))
        if "append" in y:
            list.append(int(y[1]))
        if "remove" in y:
            list.remove(int(y[1]))
        if "pop" in y:
            list.pop()
        if "reverse" in y:
            list.reverse()
        if "sort" in y:
            list.sort()
        if "print" in y:
            print(list)
            #list = []


# Solutions from site 1/2
test =int(input())
s=[]
for _ in range (test):
    cmd=list(input().split())
    
    if cmd[0]=='insert':
        s.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))
    elif cmd[0]=="append":
        s.append(int(cmd[1]))
    elif cmd[0]=="sort":
        s.sort()
    elif cmd[0]=="pop":
        s.pop()
    elif cmd[0]=="reverse":
        s.reverse()
    elif cmd[0]=="count":
        v=s.count(int(cmd[1]))
        print(v)
    elif cmd[0]=="index":
        x=s.index(int(cmd[1]))
        print(x)
   
    elif cmd[0]== 'print':
        print(s)


# Solutions from site 2/2
n = int(input())
a = []
for _ in range(n):
    c = input().strip()
    if c == 'print':
        print(a)
    else:
        c = c.split()
        if len(c) == 3:
            getattr(a, c[0])(int(c[1]), int(c[2]))
        elif len(c) == 2:
            getattr(a, c[0])(int(c[1]))
        else:
            getattr(a, c[0])()
        
