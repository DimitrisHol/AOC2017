import sys
handle = open("input.txt")

dictionary = dict()

for line in handle:
    line = line.rstrip()
    line = line.replace("," , "")

    tempList = list()
    tempList = line.split()
    tempList.remove("<->")

    dictionary[tempList[0]] = tempList[1:]

goal = ["0"]
for key in dictionary: # 0 , 1 ,2 , 3, 4, 5,
    flag = False;

    if key in goal:
        print("Key is in goal!")
        print("Key is : " , key , "Goal is : " , goal)
        flag = True
    if flag != True:
        for program in dictionary[key]:
            if program in goal:
                flag = True

    if flag:
        if key not in goal:
            goal.append(key)
        for program in dictionary[key]:
            if program not in goal:
                goal.append(program)

    print("Goal is now : " , goal)

print(goal)
print(len(goal))


handle.close()
