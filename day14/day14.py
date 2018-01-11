def KnotHash(x):

    length = list()
    for string in x:
    	length.append(ord(string))
    for l in [17, 31, 73, 47, 23]:
    	length.append(l)


    a = [x for x in range(256)]
    pos = 0
    skip = 0

    for index in range(64):
    	for l in length:
    		b = list()
    		steps = 0
    		while steps < l:
    			b.append(a[ (pos + steps) % len(a) ])
    			steps+=1

    		b.reverse()

    		steps = 0
    		while steps < l:
    			a[(pos+steps) % len (a)] = b[steps]
    			steps+=1

    		pos = (pos + l + skip) % len(a)
    		skip +=1


    denseHash = list()


    for index in range(16):
    	denseHashObject = a[16 * index]
    	innerIndex = 1
    	while innerIndex < 16:
    		denseHashObject = denseHashObject ^ a[16 * index + innerIndex]
    		innerIndex +=1

    	denseHash.append(denseHashObject)
    hexHash = list()

    for number in denseHash:
        if (len(hex(number)) == 3):
            hexHash.append("0" + hex(number)[2:])
        else:
            hexHash.append(hex(number)[2:])


    result = ""
    for string in hexHash:
    	result += string


    return result


def part1():
    ans =0
    for index in range(128):
        x = inp + "-" + str(index)
        goal =  ""
        for hexadecimal in KnotHash(x):
            goal += format(int(hexadecimal , 16), "04b")
        ans  += list(goal).count("1")

    print(ans)

def part2():

    grid = list()
    for index in range(128):
        x = inp + "-" + str(index)
        goal =  ""
        for hexadecimal in KnotHash(x):
            goal += format(int(hexadecimal , 16), "04b")
        grid.append(goal)

    vis = set()
    for i in range(128):
        for j in range(128):
            if (grid[i][j] == 1 and grid[i][j] not in vis):


 #-------------------------------- ACTUAL PROGRAM IS HERE -------------------------#
handle = open("inputX.txt")
inp = handle.read().rstrip()
# part1()
part2()

handle.close()

#-------------------------------- ACTUAL PROGRAM IS HERE -------------------------#
