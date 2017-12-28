import operator

def checkOP(op ,a ,b):
    # print(a, b)
    if op == ">":
        # print("GREATER THAN")
        return (operator.gt(a , b))
    elif op == "<":
        # print("LESS THAN")
        return (operator.lt(a , b))
    elif op == ">=":
        # print("GREATER EQUAL")
        return (operator.ge(a , b))
    elif op == "<=":
        # print("LESS EQUAL")
        return (operator.le(a , b))
    elif op == "==":
        # print("EQUAL")
        return (operator.eq(a , b))
    elif op == "!=":
        # print("NOT EQUAL")
        return (operator.ne(a , b))

handle = open("input.txt")
values = dict()

for line in handle:
    line = line.rstrip().split()
    line[2] = int(line[2])


    try:
        values[line[0]]
    except KeyError:
        values[line[0]] = 0
        #THIS IS NOT DEFINED
    try:
        values[line[4]]
    except KeyError:
        values[line[4]] = 0
        #THIS IS NOT DEFINED

    # print(values[line[4]], line[5] , line[6])
    # print(checkOP(line[5], values[line[4]] , int(line[6])))
    # print (line)
    if line[1] == "inc":
        if (checkOP(line[5], values[line[4]] , int(line[6]))):
            values[line[0]] += line[2]
    else:
        if (checkOP(line[5], values[line[4]] , int(line[6]))):
            values[line[0]] -= line[2]


# print(values)
max = None;
for value in values:
    if max == None:
        max = values[value]
    elif max < values[value]:
        max = values[value]
print(max)
handle.close()



# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
