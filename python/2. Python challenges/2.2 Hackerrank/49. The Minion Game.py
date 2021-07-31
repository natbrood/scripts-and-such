# https://www.hackerrank.com/challenges/the-minion-game/problem

#My script, way too slow

def minion_game(string):
    stoploop,rounds,singleround,n,totalStuart,totalKevin,newstring = False,0,0,0,0,0,""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    #calculate the amount of rounds
    n = len(string)
    while stoploop == False:
        if n != 0: 
            rounds += n
            n -= 1
        else:
            stoploop = True

    #n = 0 atm
    for x in range(rounds+len(string)):
        if singleround < len(string)-n:
            try:
                newstring += string[singleround+n]

                if(newstring[0] not in vowels):
                    totalStuart += 1
                else:
                    totalKevin += 1
                singleround += 1
                
            except Exception:
                print("Out")

        elif singleround == len(string)-n: 
            newstring = ""
            n += 1
            singleround = 0
    
    if(totalStuart > totalKevin):
        print("Stuart",totalStuart)
    elif (totalStuart < totalKevin):
        print("Kevin",totalKevin)
    else:
        print("Draw")
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)


# Solutions from site
def minion_game(string):
    scores = {"Kevin": 0, "Stuart": 0}
    for i in range(len(string)):
        if string[i] in "AEIOU":
            scores["Kevin"]+=len(string)-i
        else:
            scores["Stuart"]+=len(string)-i
    if scores["Stuart"] == scores["Kevin"]:
        print("Draw")
    elif scores["Stuart"] > scores["Kevin"]:
        print("%s %s" %("Stuart", scores["Stuart"]))
    else:
        print("%s %s" %("Kevin", scores["Kevin"]))


if __name__ == '__main__':
    s = input()
    minion_game(s)
