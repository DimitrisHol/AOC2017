handle = open("input.txt")
x = handle.read()
goal = list()
length = len(x)
removedChars = 0
index = 0
flag = True
while index < len(x):
		if x[index] == "!":
			index +=1
		elif x[index] == "<":
			if not flag:
				removedChars +=1
			flag = False
		elif x[index] == ">":
			flag = True
		else:
			if flag:
				goal += x[index]
			else:
				removedChars +=1
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
print("Score:" ,count)
print("Removed chars: " , removedChars)

handle.close()
