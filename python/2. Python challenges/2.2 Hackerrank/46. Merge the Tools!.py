# https://www.hackerrank.com/challenges/merge-the-tools/problem

from textwrap import wrap

def merge_the_tools(string, k):
    raw = wrap(string, k)
    for x in raw:
        print("".join(dict.fromkeys(x)))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


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
