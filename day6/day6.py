#opening the file
handle = open("input.txt")

for line in handle:
    banks = line.split()

#Converting to ints
for index in range(len(banks)):
    banks[index] = int(banks[index])

# banks = [0, 2, 7, 0]

configs = list()
cycles = 0

config = ""
for bank in banks:
    config += str(bank)

while (True):
    if (config in configs):
        break;
    else:
        configs.append(config)
    #----------------------------------------------
    #Distribute

    #----DEBUG----
    print("Currently the list is : " , banks)
    #-------------
    maxBank = banks.index(max(banks))
    points = banks[maxBank]
    banks[maxBank] = 0
    #----DEBUG----
    print("Position of the max bank is : " , maxBank)
    print("Points : " , points)
    #-------------
    index = (maxBank +1) % len(banks)

    while (points > 0):
        #----DEBUG----
        print("Points : " , points)

        #-------------
        banks[index] +=1
        points -=1
        index = (index + 1) % len(banks)

    #----------------------------------------------
    cycles +=1

    config = ""
    for bank in banks:
        config += str(bank)

print(cycles)
