# https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = list(dict.fromkeys(sorted(input())))
    #print(s)
    x1,x2,x3,x4,x5 = 0,0,0,0,0
    
    for x in list(s):
        if x.isalnum() and x1 == 0:
            x1 += 1
        if x.isalpha() and x2 == 0:
            x2 += 1
        if x.isdigit() and x3 == 0:
            x3 += 1
        if x.islower() and x4 == 0:
            x4 += 1
        if x.isupper() and x5 == 0:
            x5 += 1
    print(x1==1)
    print(x2==1)
    print(x3==1)
    print(x4==1)
    print(x5==1)


# Solutions from site 1/2
inp = input()
print(any(x.isalnum() for x in inp))
print(any(x.isalpha() for x in inp))
print(any(x.isdigit() for x in inp))
print(any(x.islower() for x in inp))
print(any(x.isupper() for x in inp))


# Solutions from site 2/2
str = str(input())
def f(x,str):
    res = False
    for i in str:
        res = res or getattr(i,x)()
    return res

print(f("isalnum",str))
print(f("isalpha",str))
print(f("isdigit",str))
print(f("islower",str))
print(f("isupper",str))
