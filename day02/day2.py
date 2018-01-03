handle = open("input.txt")
gridList = list()
sum = 0
for line in handle:
    newStringList = list()
    newIntList = list()
    newStringList = line.split()
    for element in newStringList:
        newIntList.append(int(element))

    print(max(newIntList) , min(newIntList))
    checksum = max(newIntList) - min(newIntList)
    sum += checksum
print(sum)
handle.close()
