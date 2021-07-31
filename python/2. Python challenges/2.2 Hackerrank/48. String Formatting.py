# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    s = len(bin(n)[2:]) #rjust is the lenght of the longest binary
    for x in range(1,number+1):
        print("{} {} {} {}".format(str(x).rjust(s),str(oct(x))[2:].rjust(s),
                                                   str(hex(x)).upper()[2:].rjust(s),
                                                   str(bin(x))[2:].rjust(s)))

    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Solutions from site 1/2
def bina(n):
    rep = bin(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep


def inta(n):
    rep = str(n)
    pad = m - len(rep)
    return pad * " " + rep + " "


def octa(n):
    rep = oct(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep + " "


def hexa(n):
    rep = hex(n)[2:].upper()
    pad = m - len(rep)
    return pad * " " + rep + " "

k = int(input())
m = len(bin(k).lstrip("0b"))

for i in range(1, k+1):
    r = [inta(i), octa(i), hexa(i), bina(i)]
    print("".join(r))


# Solutions from site 2/2
N = int(input())
l = len(bin(N)) - 2

for i in range(1, N + 1):
    f = ""
    for c in "doXb":
        if f:
            f += " "
        f += "{:>" + str(l) + c + "}"
    print(f.format(i, i, i, i))
