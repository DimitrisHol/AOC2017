handle = open("input.txt" , "r")

inp = handle.read()
inp.rstrip()

#TESTING
#inp = "1212"
#inp = "1221"
#inp = "123425"
#inp = "123123"
#inp = "12131415"

"""
if list contains 10 items

include the digit 10/2 = 5 steps forward

1212 , len = 4 so 4/2 = 2 steps forward

index = 0 --> pair = index = 0+2 = 2 , 4 % 2 = 2
index = 2 --> pair = index = 1+2 = 3 , 4 % 3 = 3
index = 1 --> pair = index = 2+2 = 4 , 4 % 4 = 0
index = 3 --> pair = index = 3+2 = 5 , 5 % 4 = 1

num1 = index
num2 = len % index + len/2

pairs :

(0 , 2) = 1 ,1 Sum = 0+1 = 1
(1 , 3) = 2 ,2 Sum = 1+2 = 3
(2 , 0) = 1 ,1 Sum = 3+1 = 4
(3 , 1) = 2 ,2 Sum = 4+2 = 6


INDEX = 0 1 2 3
STR   = 1 2 1 2

"""


sum = 0
length = len(inp)
print("----------------------------------------------")


print("Input is : " , inp)
for index in range(length-1):
    num1 = inp[index]
    index2 = int(int(index + length/2) % length)
    num2 = inp[index2]
    print ("Index =" , index, "input = ",inp[index], "input2 = ",inp[index2])
    if (num1 == num2):
        print("SUCCESS!")
        print("Sum was : " , sum)
        sum += int(inp[index])
        print("Sum is : " , sum)

print ("Final sum = " ,sum)
print("----------------------------------------------")


handle.close()


# 1278 too high