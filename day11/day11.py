import math

handle = open("input.txt")
x = handle.read().rstrip()
path = x.split(",")
x = y = z =  0
max = None
for d in path:
	if (d == "n"):
		y +=1
		z -=1
	elif(d == "ne"):
		x +=1
		z -=1
	elif(d == "nw"):
		y +=1
		x -=1
	elif(d == "s"):
		z +=1
		y -=1
	elif(d == "se"):
		x +=1
		y -=1
	elif(d == "sw"):
		z +=1
		x -=1
	currentDistance = (abs(x) + abs(y) + abs(z)) /2
	if max is None:
		max = currentDistance
	elif currentDistance > max:
		max = currentDistance

x = abs(x)
y = abs(y)
z = abs(z)

print("Current Distance = " ,int ((x+y+z) /2))
print("Max distance is : " , max)

handle.close()
