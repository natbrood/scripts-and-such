# https://www.hackerrank.com/challenges/list-comprehensions/problem

# Note, this one is quite slow and does a lot of redundant things. Didn't pass the checks on the site
if __name__ == '__main__':
    x,y,z,n = int(input()),int(input()),int(input()),int(input())
    a,b,c = 0,0,0
    
    thislist = [[0,0,0]]
        
    while a <= x:
        if c < x:
            c += 1
            if a+b+c != n:
                thislist.append([a,b,c])
        else:
            if b < x:
                c = 0
                b += 1
                if a+b+c != n:
                    thislist.append([a,b,c])
            else:
                if a < x:
                    c = 0
                    b = 0
                    a += 1
                    if a+b+c != n:
                        thislist.append([a,b,c])
                else:
                    break
                    
    print(thislist)


# Solutions from site
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)
