#opening the file
handle = open("input.txt")

for line in handle:
    banks = line.split()

#Converting to ints
for index in range(len(banks)):
    banks[index] = int(banks[index])

#banks = [0, 2, 7, 0]

configs = list()
cycles = 0

config = ""
for bank in banks:
    config += str(bank)
print("Start cycle is   : " , banks)
while (True):
    if (config in configs):
        configs.append(config)
        break;
    else:
        configs.append(config)
    #----------------------------------------------
    #Distribute
    maxBank = banks.index(max(banks))
    points = banks[maxBank]
    banks[maxBank] = 0
    index = (maxBank +1) % len(banks)

    while (points > 0):
        banks[index] +=1
        points -=1
        index = (index + 1) % len(banks)

    #----------------------------------------------
    # print("Current cycle is : " , banks)
    cycles +=1

    config = ""
    for bank in banks:
        config += str(bank)

print("Total cycles are : " , cycles)
for index in range(len(configs)):
    if (config == configs[index]):
        print("Size of the loop : ",len(configs) - index -1)
        break;

handle.close()
