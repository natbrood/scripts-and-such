# https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    #mark = ""
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    grades = [y for x,y in student_marks.items() if x == query_name]
    
    for a,b,c in grades:
        print(format((a+b+c)/3, '.2f'))
        
    #line 13+14 could be done easier, I suppore. In something like:
    #print(format((a+b+c)/3, '.2f') for a,b,c in grades)


# Solutions from site 1/2
N = int(input())
stud_dict = dict()

for i in range(N):
    tmp = input().split(' ')
    name = tmp[0]
    stud_dict[name] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))
    
name = input()
print('%.2f' % (sum(stud_dict[name]) / 3.0))


# Solutions from site 2/2
data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
marks = data[input()]
print("%.2f" % (sum(marks)/len(marks)))

# https://www.datacamp.com/community/tutorials/role-underscore-python
