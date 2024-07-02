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