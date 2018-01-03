handle = open('input.txt')
names = list()
bad = set()
weights = {}
for line in handle:
    line = line.rstrip().split()
    names.append(line[0])
    if ( "->" in line):
        for child in line[3:]:
            bad.add(child.strip(","))

for name in  names:
    if (name not in bad):
        root = name

print (root)

handle.close()
