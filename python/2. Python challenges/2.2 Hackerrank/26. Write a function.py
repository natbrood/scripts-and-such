# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = True
    notleap = False
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                return leap
        else:
            return leap
    return False

    
    #1990
year = int(input())
print(is_leap(year))


# Solutions from site 1/2
def is_leap(year):
    leap = False
    
    if (year % 100 == 0) and (year % 400 == 0):
        leap = True
    return leap


# Solutions from site 2/2
def is_leap(year):
    leap = False
    if not year%400 : 
        return True
    if not year%100 : 
        return False
    if not year%4 : 
        return True
    return False
    return leap
