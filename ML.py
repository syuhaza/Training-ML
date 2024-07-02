# def checkPrimeNumber(num):

#   primes = []
#   for a in range(2, num):
#         isPrime =  True
#         for b in range(2, a):
#             if a % b == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             primes.append(a)
  
#   for i in range(len(primes) - 1):
#         if primes[i + 1] - primes[i] == 2:
#             print("(", primes[i], ",", primes[i + 1], ")", end=' ')


# num = 50
# checkPrimeNumber(num)


# def checkPrimeNumber(num):
#     primes = []
    
#     for i in range(2, num):
#         isPrime = True
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             primes.append(i)
    
#     for i in range(len(primes) - 1):
#         if primes[i + 1] - primes[i] == 2:
#             print("(", primes[i], ",", primes[i + 1], ")", end=' ')

# num = 50
# checkPrimeNumber(num)

# def primeFactors(num):

#   factors = []
#   divisor = 2

#   while num > 1:
#     while num % divisor == 0:
#       factors.append(divisor)
#       num //= divisor
#     divisor += 1
#   return factors


# num = int(input("Enter a number:"))
# factors = primeFactors(num)
# print(f"The prime factors of {num}: {factors} ")

# def findMaxandMin(*args):

#   maxNum = args[0]
#   minNum = args[0]

#   for num in args[1:]:
#       if num > maxNum:
#         maxNum = num
#       if num < minNum:
#         minNum = num

#   return minNum, maxNum


# minNum, maxNum = findMaxandMin(*args)

# print(minNum, maxNum)

# """ Set """
# a=(0,1,2,3,4)
# b=slice(1,2) # the indices from start, and not included the end
# print(a[b]) 

# a=(1,2,(4,5))
# b=(1,2,(3,4))
# print(a>b)

# # x = {1, 2, 3}
# # y = {1, 2}
# # y.ispropersubset(x) there will be error bcause there no ispropersubset()

# s = {'foo', 'bar', 'baz', 'qux'}

# # Following that remove the element 'bar' from s
# # s.discard('bar')
# # s &= {'foo','baz','qux'}
# # s -= {'bar'}

# d = {"john":40, "peter":45}
# "john" in d

# # frozensets
# # can be a member of a set, and can serve as a dictionary key
# # If f is a frozen set, statement f.add('foo') will raise an exception

# a=(1,2,3)
# b=('A','B','C')
# c=zip(a,b)      #returns Zip Object
# print(list(c)) # Output will be 
# # [(1,'A'),(2,'B'),(3,'C')]


# def make_palindrome(s):
#     mid = len(s) // 2
#     first_half = s[:mid]
#     second_half = first_half[::-1]
#     if len(s) % 2 == 0:
#         return first_half + second_half
#     else:
#         return first_half + s[mid] + second_half

# s = input("Enter a string: ")
# print(make_palindrome(s))

# palinString = input("")

# if palinString == palinString[::-1]:
#     print(palinString[::-1])
# else:
#     newString = palinString.replace(palinString[2], palinString[::-1])
#     print(newString)

# def valueRoman(r):
#     if r == "I":
#         return 1
#     if r == "V":
#         return 5
#     if r == "X":
#         return 10
#     if r == "L":
#         return 50
#     if r == "C":
#         return 100
#     if r == "D":
#         return 500
#     if r == "M":
#         return 1000
#     return -1

# def printRoman(s):
#     result = 0
#     i = 0
#     while i < len(s):
#         string1 = valueRoman(s[i])
#         if i + 1 < len(s):
#             string2 = valueRoman(s[i + 1])
#             if string1 < string2:
#                 result += string2 - string1
#                 i += 2
#             else:
#                 result += string1
#                 i += 1
#         else:
#             result += string1
#             i += 1
#     return result

# def intRoman(num):
#     value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     symbol = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
#     roman_num = ''
#     i = 0
#     while  num > 0:
#         for _ in range(num // value[i]):
#             roman_num += symbol[i]
#             num -= value[i]
#         i += 1
#     return roman_num

# convertRomanOrNumeral = input("Enter an integer number or Roman numeral: ")

# if convertRomanOrNumeral.isdigit():
#     result = intRoman(int(convertRomanOrNumeral))
#     print("The Roman numeral for number: ", result)
# else:
#     result = printRoman(convertRomanOrNumeral.upper())
#     print("The number of the Roman numeral: ", result)


# # get set from user
# set1 = list(map(int, input().split(",")))   
# set2 = list(map(int, input().split(",")))   

# set1 = set(set1)
# set2 = set(set2)

# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))

# # User input using dictionary
# numClients = int(input("Enter the number of clients\n"))

# detailsClient = {}
# for i in range(1, numClients + 1):
#     name = input(f"Enter the details of the client {i}\n")
#     email = input("")
#     passportNum = input("")
#     detailsClient[passportNum] = f"\n{name}--{email}--{passportNum}"

# searchPassNum = input("Enter the passport number of the client to be searched\n")

# if searchPassNum in detailsClient:
#     print(f"Client Details\n")
#     print(detailsClient[searchPassNum])
# else:
#     print("Client not found")


# ##############################
# def Odd(a, b):
#     if a & 1 and b &1:
#         print("Both are Odd")
#     elif(a&1):
#         print("%d is Odd"%(a))
#     elif(b&1):
#         print("%d is Odd"%(b))
# Odd(3, 4)

# def C2F(c):
#     return(c * 9//5 + 32)
# print(C2F(100)),
# print(C2F(0))

from datetime import datetime 

def calculateDatetime():

    date1 = input()
    date2 = input()

    # date = datetime.strptime(time_data, format_data)
    date1 = datetime.strptime(date1, "%b %d %Y %I:%M%p")
    date2 = datetime.strptime(date2, "%b %d %Y %I:%M%p")

    delta = date2 - date1

    # Extract the number of days
    days = delta.days
    # divmod - calculate quotient and remainder
    # quotient, remainder = divmod()
    # delta.second - return the number of seconds

#######################################################################
#######################################################################
#######################################################################
# Simplify code
numSheet = int(input("Enter total Number of sheets:"))

attendanceSheet = []
for i in range(numSheet):
    # need to stored the register number into  tuple
    # append only for list
    # convert from list to tuple
    registerNum = tuple(map(int, input().split(" ")))
    attendanceSheet.append(registerNum)

print("Attendance Sheets with Register Number:", attendanceSheet)
# convert the tuple into set of a uniques
# 1) map(set, attendanceSheet)
# 2) set.union(*map(set, attendanceSheet))
# * operator  is used to unpack  the set generated by map
# set.union - - method to find the union
# tuple - converted the result of set.union back into tuple
print("Final sheet: ", tuple(set.union(*map(set, attendanceSheet))))

############################################################################
# expand code
numSheet = int(input("Enter total Number of sheets:"))

attendanceSheet = []
for i in range(numSheet):
    registerNum = tuple(map(int, input().split(" ")))
    attendanceSheet.append(registerNum)

# convert each of the tuple into set
sets = map(set, attendanceSheet)
# Find union from all the set
# * operator open the list bracket and we have all each set without a list
union_set = set.union(*sets)

tupleSheet  = tuple(union_set)

print("Attendance Sheets with Register Number:", tuple(attendanceSheet))
print("Final sheet:", tupleSheet)


