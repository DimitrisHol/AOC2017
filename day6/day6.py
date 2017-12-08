# 16 memory banks
# each holds any number of blocks

#16 x bank >> blocks

def distribute():
    pass
def maxDict(dict):

    maxValue = None
    maxBank = None
    for bank in dict:
        # print("maxValue =" , maxValue , "maxBank = " ,maxBank)
        # print("bank=",bank , "bankValue" ,dict[bank])
        if (maxValue is None):
            maxValue = dict[bank]
            maxBank = bank
        elif (dict[bank] > maxValue):
            maxValue = dict[bank]
            maxBank = bank
        #IF THEY HAVE THE SAME # OF BLOCKS, MAX IS THE FIRST ONE
        elif (dict[bank] == maxValue):
            maxBank= min(bank, maxBank)
            maxValue = dict[min(bank, maxBank)]
    return maxValue

memoryBanks = dict()

memoryBanks["bank0"] = 2
memoryBanks["bank1"] = 2
memoryBanks["bank2"] = 2
memoryBanks["bank3"] = 3

flag = True
configs = list()

config = ""
for bank in memoryBanks:
    config += str(memoryBanks[bank])
configs.append(config)

print(config)
print(configs)

memoryBanks["bank0"] = 3
memoryBanks["bank1"] = 3
memoryBanks["bank2"] = 3
memoryBanks["bank3"] = 4

#while (flag):

config = ""
for bank in memoryBanks:
    config += str(memoryBanks[bank])

print(configs)
if (config in configs):
    flag = False
else:
    configs.append(config)

#distribute(memoryBanks)

print(config)
print(configs)
print(flag)
