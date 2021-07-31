# https://www.hackerrank.com/challenges/nested-list/problem

# First try
if __name__ == '__main__':
    listing = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listing.append([name,score])
        scores.append(score)
    #minscore = min(scores) 
    
    sortedlist = sorted(listing, key=lambda x: x[::-1]) #Sorts the list based on value
    #[['Tina', 37.2], ['Berry', 37.21], ['Harry', 37.21], ['Harsh', 39.0], ['Akriti', 41.0]]
    

    uglydeleted = 0
    uglysolution = 0
    uglynumber = ""
    for x,y in sortedlist:
        #print(int(y)+1)
        if uglydeleted != 1:
            listing.pop(0)
            uglydeleted += 1
        else:
            if uglysolution != 1: #and max(0,int(y))!=0:
                uglynumber = y
                print(x)
                #print(sortedlist)
                uglysolution += 1
            elif uglynumber == y:
                print(x)

# Solution
#take value of n
no_of_students = int(input())
#create empty list
records = []
#append record of each student name,score in a for loop
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])

#convert list of records to a python dictionary
# [['Harry', 37.21], ['Berry', 37.21]] becomes 
# {'Harry': 37.21, 'Berry': 37.21}
records = dict(records)
#get only values from our dictionary and use set function to rmeove duplicate score then sort it in ascending order
scores = sorted(set(records.values()))
#index 1 has the 2nd lowest score
second_lowest_score = scores[1]
#create a list of names of students who has 2nd lowest score using list comprehension
second_lowest_students = [name for name,score in records if score==second_lowest_score]
#sort names in alphabetical order
second_lowest_students.sort()
#loop through each name and print
for name in second_lowest_students:
    print(name)



# Shorter version
students = [[input(),float(input())] for i in range(int(input()))]
second_highest = sorted(set(j for i,j in students))[1]
print("\n".join(sorted(i for i,j in students if j==second_highest)))
