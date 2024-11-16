"""
1. Character Deletion in a string
"""
inputString = input("")
index = int(input())   

newstring = inputString.replace(inputString[index-1], "" )

print(newstring)

"""
2. Print Palindrome
"""
s = input(" ")

mid = len(s) // 2
firstHalf = s[:mid]
secHalf = firstHalf[::-1]

if(s == s[::-1]):
    print(s[::-1])
elif(len(s) % 2 == 0):
    print(firstHalf + secHalf)
else:
    print(firstHalf + s[mid] + secHalf)

"""
3. Pattern Printing
"""
num = int(input())

pattern = "/" *num + '\\' *num + "/" *num + '\\' *num
for i in range(4):
    print(pattern)

"""
4. Concatenation of Strings
"""
firstStr = input("Enter the first string:")
secStr = input("Enter the second string:")

if firstStr[0] == secStr[0]:
    print(firstStr + " " +  secStr)
else:
    print("Invalid Input")

"""
5. find a total number of books required and total cost of required books
"""
totalSchool = int(input())

totalStudent = 0
for i in range(totalSchool):
    numStudent = int(input())
    totalStudent += numStudent

priceBooks = int(input())

totalOverall = totalStudent * priceBooks
print(f"Total number of books required: {totalStudent}")
print(f"Total cost: {totalOverall}")

"""
6. Symmetric Difference
"""
set1 = input()
set2 = input()

numList = set(int(x) for x in set1.split(","))
numList2 = set(int(x) for x in set2.split(","))

if numList != numList2:
    print(numList.symmetric_difference(numList2))
else:
    print("invalid set")

"""
7. Date Difference
"""
from datetime import datetime as dt

dateFormat =  "%b %d %Y %I:%M%p"

date1 = dt.strptime(input(), dateFormat)
date2 = dt.strptime(input(), dateFormat)

delta = date2 - date1

print(delta) 
# delta - extract days and time

"""
8. Duplicate Attendance
"""
numSheet = int(input("Enter total Number of sheets:"))

attendanceSheet = []
for i in range(numSheet):
    registerNum = tuple(map(int, input().split(" ")))
    attendanceSheet.append(registerNum)

# convert each of the tuple into set
sets = map(set, attendanceSheet)
# Find union from all the set
union_set = set.union(*sets)
tupleSheet  = tuple(union_set)

print("Attendance Sheets with Register Number:", tuple(attendanceSheet))
print("Final sheet:", tupleSheet)

"""
9. Second Highest Mark of Student
"""
numStudent = int(input())

studentMarks = {}
for i in range(numStudent):

    name, *marks = input().split()
    if name not in studentMarks:
        studentMarks[name] = []
    studentMarks[name]  = list(map(int, marks))

studentName = input()
if studentName not in studentMarks:
    print("Student doesn't exist")
else: 
    markSt = studentMarks[studentName]
    if len(set(markSt)) == 1:
        print(f"{studentName} scored same marks in all subjects: {markSt[0]}")
    else:
        markSt = sorted(markSt)
        print(f"Second Highest mark of {studentName}: {markSt[-2]}")

"""
10. Words count
"""
sentenceInput = input()

words = sentenceInput.split()
wordsDict = {}
for word in words:
    if word in wordsDict:
        wordsDict[word] += 1
    else:
        wordsDict[word] = 1

print(wordsDict)

""" Airline Client Details
Input and Output Format:
Refer to sample input and output for formatting specifications.
print “Client not found” if search not found. else print the details as in the mentioned format below.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output 1:
Enter the number of clients
2
Enter the details of the client 1
Shri
shri@mail.com
7346218
Enter the details of the client 2
Veena
veena@mail.com
8639124
Enter the passport number of the client to be searched
7346218
Client Details
Shri--shri@mail.com--7346218
"""


""" Decoding Secret Message
Raj knows the way to decode the string. Decoding format is he has to reverse the string and he has to take out a substring from range N to M(from Nth position to Mth position and string position starts from 0) and password contains last digits which are Ascii value of first 2 characters of the non-reversed string.
Help him decode the string.

Input format
1st input is a string indicates a secret message.
2nd input is an integer indicates starting range of message.
3rd input is an integer indicates ending range of message.

Output format
The output is a string indicates password of Computer. [last digits of a password should be like Ascii value of the last character first and Ascii value of the last 2nd character is next].

All text in bold corresponds to the input and the rest corresponds to output [Refer sample input and output format].

Sample Input and Output 1
Enter Secret Message
saaathtrrrkksu
Enter Starting Range
3
Enter Ending Range
7
Password: krrrt11597
"""