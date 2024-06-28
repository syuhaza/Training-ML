# amount = int(input("Please enter the withdrawal amount: "))

# note50 = amount // 50
# amount = amount % 50
# note20 = amount // 20
# amount = amount % 20
# note10 = amount // 10
# amount = amount % 10
# note1 = amount // 1

# if((amount % 10) == 0):
#     print("The amount is a multiple of 10.")
#     print("Total note 50: ",note50)
#     print("Total note 20: ",note20)
#     print("Total note 20: ",note10)
#     print("Total note 20: ",note1)
# else:
#     print("Error amount withdrawal.")

# # print("Total note 50: ",note50)
# # print("Total note 20: ",note20)
# # print("Total note 20: ",note10)
# # print("Total note 20: ",note1)

# num = int(input("Please enter the number: "))

# r2 = num ** 2

# numList = input()

# olderList = numList.split(",")
# newList = []

# for i in olderList:
#     if i in newList:
#         continue
#     elif i not in newList:
#         newList.append(i)
# print(newList)

# import sys

# numbers = sys.argv[1:]
# print(numbers)

# print("Display all elements: ")
# for number in numbers:
#     print(number, end=' ')
# print()

# print("Elements in even positions: ")
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         print(numbers[i], end=' ')
# print()

# print("Elements in odd positions: ")
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         print(numbers[i], end=' ')
# print()


# n = input()

# numTurn = n.split(" ")

# A, B, N = numTurn[0], numTurn[1], numTurn[2]

# if N == A:
#     turns = int(A)*2
#     sumScore = turns + int(B)
# elif N == B:
#     turns = int(B)*2
#     sumScore = turns + int(A)

# print(sumScore)

# strInput = input("Enter numbers separated by commas: ")

# numbers = strInput.split(",")
# print(numbers)

# result = True
# for a in range(len(numbers)):
#     for b in range(a+1, len(numbers)):
#         if numbers[a] == numbers[b]:
#             result = False
#             break
#     # if not result:
#     #   break

# if result:
#   print("The numbers are different")
# else:
#   print("The numbers have duplicate")

# a = int(input())
# b = int(input())


# for i in range(a , b + 1):
#         if(i > 0):
#             isPrime = True
#             for j in range(2, i):
#                     if(i % j == 0):
#                         isPrime = False
#                         break
#             if(isPrime == True):
#                     print(i, end=" ")

# firstNum = int(input("Enter first integer: "))
# secNum = int(input("Enter second integer: "))

# GCDList = []

# if firstNum > secNum:
#   numA, numB = firstNum, secNum
# else:
#   numA, numB = secNum, firstNum 

# num_A, num_B = numA, numB
# GCDList.append((num_A,num_B))

# while num_A > 0:
#   r = num_A % num_B
#   num_A, num_B = num_B, r
#   GCDList.append((num_A,num_B))
#   if num_A == 0:
#     result = num_B
#     break
#   elif num_B == 0:
#     result = num_A
#     break

# print(GCDList)
# print(f"GCD{numA,numB}: {result}")


# count = 10
# for a in range(2,60):
#     isPrime =True
#     for i in range(2,a):
#         if(a%i==0):
#             isPrime = False
#             break
#     if(isPrime == True):
#         perfectNum = ((2**(a - 1)) * ((2**a)-1))  # formula perfect number: 2**p-1(2**p -1)
#         for i in range(1,100):
#              number % i == 0
#         # print(perfectNum)
#         if perfectNum % i == 0:
#           count = count - 1
#     if count == 0:
#       break


# def sum(a,b):
#     return a + b
# # print(sum(10,20))

# # reminder when we see "function(value)" we always call values as argument
# # in the above statement it looks we are passing

# def minus(a,b):
#     return a - b

# """def arithematic(keyword, a, b):
#     if keyword == "s":
#         return sum(a,b)
#     elif keyword == "m":
#         return minus(a,b)
# """
# # arithematic("s", 10, 20)
# # notice no there is no () after the function name
# # this is how you pass function as an argument to another 
# def arithematic(func, a, b):
#     return func(a,b)
    
# # arithematic(minus, 10, 20)
# print(arithematic(sum, 10, 20))
# print(arithematic(minus, 10, 20))


# def mul(a,b):
#     return a * b
# print(arithematic(mul, 10, 20))




def numberToWord(num):

    if num == 0:
      return "The number is zero"

    words = ""
    firstDigit = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    teenDigit = ["Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eightteen","Nineteen"]
    tensDigit = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if num >= 1000:
      words += firstDigit[num // 1000-1] + " thousands "
      num = num % 1000
    if num >= 100:
      words += firstDigit[num // 100-1] + " hundred " 
      num %= 100
    if num >= 11 and num <= 19:
      words += " and " + teenDigit[num-11] + " "
      num = 0
    elif num >= 20:
      words += " and " + tensDigit[num//10] + " "
      num %= 10 
    if num >= 1 and num <= 10:
        words += firstDigit[num-1] + " "
    return words


num = int(input("Enter a number to convert into words: "))

words = numberToWord(num)

print("The words representation of the number: ", words)

