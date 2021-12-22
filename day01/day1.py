handle = open("input.txt" , "r")

inp = handle.read()
inp.rstrip()

#Testing
#inp = "1122"
#inputs = list()
#inputs = ["1122" , "1111" , "1234" , "91212129"]
#inp = "91212129"

# Iterate throught the string
# If string[index] == string[index +1]
# sum += string[index].parseToInt

sum = 0
print("----------------------------------------------")
#print("Input is : " , inp)
for index in range(len(inp) -1):
#    print ("Index =" , index, "input = ",inp[index], "input2 = ",inp[index+1] )
    if(inp[index] == inp[index +1]):
#        print("SUCCESS!")
#        print("Sum was : " , sum)
        sum += int(inp[index])
#        print("Sum is : " , sum)

#print ("input0 = ",inp[0], "lastInput = ",inp[len(inp)-1] )
if inp[len(inp)-1] == inp[0]:
#    print("SUCCESS!")
#    print("Sum was : " , sum)
    sum += int(inp[0])
#    print("Sum is : " , sum)
#print ("first one : " , inp[0] , "last one :" ,inp[len(inp)-2] )
# print (inp[2135] , inp[0])
print (len(inp))
print ("Final sum = " ,sum)
print("----------------------------------------------")

handle.close()
