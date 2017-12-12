handle = open("input.txt")
lst = list()
for line in handle:
    lst.append(int(line.rstrip()))



#lst = [0, 3 , 0 , 1 , -3 ]
#print(lst)
index = 0
steps = 0

while (index <len(lst)):
    if (lst[index] > 3):
        lst[index] -=1
    else:
        lst[index] +=1

    index = index + lst[index] -1
    steps +=1
    #print(lst)

print(steps)
