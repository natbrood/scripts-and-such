# https://pythonprinciples.com/challenges/Online-status/

# Version 1
statuses = {"Alice": "online","Bob": "offline","Eve": "online"}

def online_count():
    statuscount = 0
    for key in statuses:
        if(statuses[key] == "online"):
            statuscount += 1
    print(statuscount)       
online_count()


# Version 2
statuses = {"Alice": "online","Bob": "offline","Eve": "online"}

def online_count(x):
    statuscount = 0
    for key in x:
        if(x[key] == "online"):
            statuscount += 1
    return statuscount     
online_count(statuses)

# Solution from site
# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])