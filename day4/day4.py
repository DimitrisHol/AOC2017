handle = open("input.txt")
count = 0
for line in handle:
    tempList = line.rstrip().split()
    for word in tempList:
        if (tempList.count(word) > 1):
            count -=1
            break;
    count +=1
print(count)
