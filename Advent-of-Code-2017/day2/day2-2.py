handle = open("input.txt")
gridList = list()
sum = 0
for line in handle:
    newStringList = list()
    newIntList = list()
    newStringList = line.split()
    for element in newStringList:
        newIntList.append(int(element))
    num1 = None
    num2 = None
    for checkNum in newIntList:
        #print("Checknum is:" , checkNum)
        for number in newIntList:
            #print("Number is:" , number)
            #print((not checkNum == number and checkNum % number == 0))
            if (not checkNum == number and checkNum % number == 0):
                num1 = checkNum
                num2 = number
                break;
            if (num1 is not None):
                break;

    if num1 > num2:
        sum += num1/num2
    else:
        sum +=num2/num1
print(sum)
