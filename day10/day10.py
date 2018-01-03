# NOTE: WIP

handle = open("input.txt")


x = handle.read().rstrip().split(",")
length = list()
for string in x:
    length.append(int(string))

pos = 0
skip = 0

itList = [0,1,2,3,4]
length = [3, 4, 1, 5]


start = 1
x = 2
print ("Start : " , itList[start:start+x])
if start == 0:
    print("End   : " , itList[x-1::-1])
else: # TODO: FIND A WAY TO MAKE THIS WORK 100%
    print("End   : " , itList[:start:-1])



# itList[:3] = itList[2::-1]




handle.close()
