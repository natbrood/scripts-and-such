# https://www.hackerrank.com/challenges/text-wrap/problem


source = input().split()


def pattern(n,m):
    dashC = -5 # 1 - the +6 from line 10 
    thingC = -1 # and 1 - +2 from line 11 to save 2 lines
    
    #first block
    for x in range(int((n-1)/2)):
        dashC += 6
        thingC += 2
        dashes = '-'*int((m-(2+dashC))/2)
        print(dashes+'.|.'*thingC+dashes)

    #welcome
    print('-'*int((m-7)/2)+"WELCOME"+'-'*int((m-7)/2))
    
    #second block
    for x in range(int((n-1)/2)):
        dashes = '-'*int((m-(2+dashC))/2)
        print(dashes+'.|.'*thingC+dashes)
        dashC -= 6
        thingC -= 2
    
pattern(int(source[0]),int(source[1]))


# Solutions from site 1/2
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
print(((M-7)//2)*'-'+'WELCOME'+((M-7)//2)*'-')
for i in range(N-2,-1,-2): 
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')


# Solutions from site 2/2
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print('---'*((N-i)//2) + '.|.'*i + '---'*((N-i)//2))
print('-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2))
for i in range(N-2,-1,-2): 
    print('---'*((N-i)//2) + '.|.'*i + '---'*((N-i)//2))
