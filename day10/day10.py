handle = open("input.txt")

x = handle.read().rstrip().split(",")
length = list()
for string in x:
    length.append(int(string))


a = [x for x in range(256)]
pos = 0
skip = 0

for l in length:
    print("Starting with : a = " , a )
    print("Selecting " , pos)
    b = list()
    steps = 0
    while steps < l:
        b.append(a[ (pos + steps) % len(a) ])
        steps+=1
        print("b =" , b)

    b.reverse()
    print("Reverse b: " , b)

    steps = 0
    while steps < l:
        a[(pos+steps) % len (a)] = b[steps]
        steps+=1

    pos = (pos + l + skip) % len(a)
    skip +=1

    print("Finishing with : a = " , a )

print(a[0]* a[1])
handle.close()
