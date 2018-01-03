from collections import*

#MAJOR THANKS TO Armav Sastry for helping me undestand this problem!

#https://www.youtube.com/watch?v=dO5ZauOP2BA

def dfs(children, weights , root):
    exp = None
    sum = weights[root]
    for child in children[root]:
        # print(child)
        weight = dfs(children, weights , child)
        sum += weight

        if exp is None:
            exp = weight
            # print( child)
        elif exp != weight:
            print("root :" , root ,"expected child" , child , "had value of " , weight , "expected"  ,exp)


    return sum



handle = open('input.txt')
names = list()
bad = set()
weights = {}
children = defaultdict(list)

for line in handle:
    line = line.rstrip().split()
    names.append(line[0])
    weights[line[0]] = int(line[1].strip("()"))
    if ( "->" in line):
        for child in line[3:]:
            children[line[0]] = [c.strip(",") for c in line[3:]]
            bad.add(child.strip(","))
for name in  names:
    if (name not in bad):
        root = name
print("the root is" ,root)

dfs(children , weights , root)

#arqoys : weight = 1859
#children : 9 + 9 = 18
# we needed 1871
#we had 1877

# so change the weight value  of arqoys to 1853

# for index in children : print(index , children[index])
# for index in weights : print(index, weights[index])
print("###############")
print("children of arqoys")
print("###############")
for child in children["arqoys"]: print(child , weights[child])

handle.close()
