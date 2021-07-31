# https://www.hackerrank.com/challenges/find-a-string/problem



# Version 1

def count_substring(string, sub_string):
    n,text,a,count = len(sub_string),list(string),0,0
    
    #print(text)
    #print(text[:-(n-1)])
    
    
    for x in text[:-(n-1)]:
        #print(text[a]+text[a+1]+text[a+2] + " == "+sub_string)
        if (text[a]+text[a+1]+text[a+2] == sub_string):
            count += 1
        a += 1
        
    if n == 4:
        a = 0
        for x in text[:-(n-1)]:
            #print(text[a]+text[a+1]+text[a+2]+text[a+3] + " == "+sub_string)
            if (text[a]+text[a+1]+text[a+2]+text[a+3] == sub_string):
                count += 1
            a += 1
    
    return count

# ====================================================================
#   This script has a way to look 'into the future' of an interation
# Despite this being cool and all.. it doesn't give the correct answer
# ====================================================================

    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# Version 2

def count_substring(string, sub_string):
    return sum(1 for i in range(len(string)) if string.startswith(sub_string, i))
        
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# Solutions from site
S = input();
ss = input();
count = 0;
for i in range(0, len(S)):
    count += S.count(ss,i,i+len(ss));
print(count);
