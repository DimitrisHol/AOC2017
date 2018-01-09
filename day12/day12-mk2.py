#DEN DOULEUEIIIII AAAAA
handle = open("input.txt")

dictionary = dict()
goal = [0]
for line in handle:
    line = line.rstrip()
    line = line.replace("," , "")

    tempList = list()
    tempList = line.split()
    tempList.remove("<->")
    #input : for example : 874 <-> 0, 1000, 1147, 1534
    #tempList - [874, 0 , 1000 , 1147, 1534]

    for program in tempList2:
        if program in goal: #if any program is connected to 0
            for p in tempList2: #connect all other programs that are not already in to 0
                if p not in goal:
                    goal.append(p)
            break

print(len(goal))
handle.close()
