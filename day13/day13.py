from collections import *

firewall = defaultdict(list)
handle = open("input.txt")

def crash(delay):
	for key in firewall:
		if (key + delay) % ((firewall[key] - 1) * 2) == 0:
			return True
	return False

def part1():
	ans = 0
	for key in firewall:
		if key % ((firewall[key] - 1) * 2) == 0:
			ans += firewall[key] * key
	return (ans)

def part2():
	delay = 0
	while (crash(delay)):
		delay+=1
	return delay

for line in handle:
	words = line.rstrip().split()
	words[0] = words[0].strip(":")
	firewall[int(words[0])] = int(words[1])


print(part1())
print(part2())





handle.close()
