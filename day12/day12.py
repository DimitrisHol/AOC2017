handle = open("input.txt")

dictionary = dict()

for line in handle:
    line = line.rstrip()
    dictionary[line[0]] = line[6:].split(", ")
    print(dictionary[line[0]])



goal = ["0"]
for index in range(250):
    for key in dictionary: # 0 , 1 ,2 , 3, 4, 5,
        flag = False;

        if key in goal:
            flag = True
        for program in dictionary[key]:
            if program in goal:
                flag = True

        if (flag):
            if not key in goal:
                goal.append(key)
            for program in dictionary[key]:
                if program not in goal:
                    goal.append(program)


print(len(goal))


handle.close()
