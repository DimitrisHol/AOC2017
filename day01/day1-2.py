handle = open("input.txt" , "r")

inp = handle.read()
inp.rstrip()

inp = '181445682966897848665963472661939865313976877194312684993521259486517527961396717561854825453963181134379574918373213732184697746668399631642622373684425326112585283946462323363991753895647177797691214784149215198715986947573668987188746878678399624533792551651335979847131975965677957755571358934665327487287312467771187981424785514785421781781976477326712674311994735947987383516699897916595433228294198759715959469578766739518475118771755787196238772345762941477359483456641194685333528329581113788599843621326313592354167846466415943566183192946217689936174884493199368681514958669615226362538622898367728662941275658917124167353496334664239539753835439929664552886538885727235662548783529353611441231681613535447417941911479391558481443933134283852879511395429489152435996669232681215627723723565872291296878528334773391626672491878762288953597499218397146685679387438634857358552943964839321464529237533868734473777756775687759355878519113426969197211824325893376812556798483325994128743242544899625215765851923959798197562831313891371735973761384464685316273343541852758525318144681364492173465174512856618292785483181956548813344752352933634979165667651165776587656468598791994573513652324764687515345959621493346623821965554755615219855842969932269414839446887613738174567989512857785566352285988991946436148652839391593178736624957214917527759574235133666461988355855613377789115472297915429318142824465141688559333787512328799783539285826471818279818457674417354335454395644435889386297695625378256613558911695145397779576526397241795181294322797687168326696497256684943829666672341162656479563522892141714998477865114944671225898297338685958644728534192317628618817551492975251364233974374724968483637518876583946828819994321129556511537619253381981544394112184655586964655164192552352534626295996968762388827294873362719636616182786976922445125551927969267591395292198155775434997827738862786341543524544822321112131815475829945625787561369956264826651461575948462782869972654343749617939132353399334744265286151177931594514857563664329299713436914721119746932159456287267887878779218815883191236858656959258484139254446341'
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
