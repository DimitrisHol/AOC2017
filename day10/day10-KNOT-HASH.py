handle = open("input.txt")

x = handle.read().rstrip()
length = list()
x = "1,2,3"
for string in x:
    length.append(ord(string))
for l in [17, 31, 73, 47, 23]:
    length.append(l)


a = [x for x in range(256)]
pos = 0
skip = 0
for index in range(64):
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

# TODO: EVERY 16 NUMBERS : XOR!!

# TODO: THE REST

handle.close()
