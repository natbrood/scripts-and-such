# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = list(map(chr, range(97, 123)))
    alphalist = alphabet[size-27::-1]+alphabet[1:size-26:-1]
    middle = []
    
    for x in range(1,size*2,2):
        middle.insert(x//2,alphalist[x//2])
        #letters * 4, -1 for single middle character, -2 for no dashes at left-right
        dashlen = ((size*4-2)-len('-'.join(middle)))//2
        print('-'*dashlen+'-'.join(middle)+'-'*dashlen)
        middle.insert(x//2,alphalist[x//2])
    
    middle.pop((len(middle)+1)//2)
    
    for y in range(1,size*2-2,2):
        middle.pop((len(middle)+1)//2)
        middle.pop((len(middle)+1)//2)
        dashlen = ((size*4-2)-len('-'.join(middle)))//2
        print('-'*dashlen+'-'.join(middle)+'-'*dashlen)

        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# Solutions from site
def gen(n):
    for i in range(n * 2 - 1):
        yield n - abs(i - n + 1)

        
n = int(input())
for i in gen(n):
    print('-'.join(chr(ord('a') + n - j) for j in gen(i)).center(n * 4 - 3, '-'))
