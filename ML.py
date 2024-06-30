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

def valueRoman(r):
    if r == "I":
        return 1
    if r == "V":
        return 5
    if r == "X":
        return 10
    if r == "L":
        return 50
    if r == "C":
        return 100
    if r == "D":
        return 500
    if r == "M":
        return 1000
    return -1

def printRoman(s):
    result = 0
    i = 0
    while i < len(s):
        string1 = valueRoman(s[i])
        if i + 1 < len(s):
            string2 = valueRoman(s[i + 1])
            if string1 < string2:
                result += string2 - string1
                i += 2
            else:
                result += string1
                i += 1
        else:
            result += string1
            i += 1
    return result

def intRoman(num):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // value[i]):
            roman_num += symbol[i]
            num -= value[i]
        i += 1
    return roman_num

convertRomanOrNumeral = input("Enter an integer number or Roman numeral: ")

if convertRomanOrNumeral.isdigit():
    result = intRoman(int(convertRomanOrNumeral))
    print("The Roman numeral for number: ", result)
else:
    result = printRoman(convertRomanOrNumeral.upper())
    print("The number of the Roman numeral: ", result)