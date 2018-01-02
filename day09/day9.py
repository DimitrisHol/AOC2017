handle = open("input.txt")
x = handle.read()
goal = list()


index = 0
flag = True
nextPass = False
while index < len(x):
    if (not nextPass):
    	if x[index] == "!":
    		index +=1
    	elif x[index] == "<":
    		flag = False
    	elif x[index] == ">":
    		flag = True
    	else:
    		if flag:
    			goal += x[index]
    	index +=1

x = "".join(goal)

count = 0
multi = 0

for character in x:
    if character == "{":
        multi +=1
    elif character == "}":
        count +=multi
        multi -= 1

print(x)
print(count)
