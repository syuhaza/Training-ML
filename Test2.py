# num = int(input("Please enter a number: "))

# square_num = num ** 2
# rev_num = int(str(num)[::-1])  # Reverse the number and convert it to int

# square_rev = rev_num ** 2

# if square_rev == int(str(square_num)[::-1]):
#     print(num, "is an ADAM Number.")
# else:
#     print(num, "is not an ADAM Number.")


# for i in range(0, 5):    
#     # Here, we are declaring an inner loop to handle number of columns    
#     # Here, the values are changing according to outer loop    
#         for j in range(0, i + 1):    
#             # Here, we are declaring a for loop for printing stars    
#             print("* ", end="")       
#         # Here, we are giving the ending line after each row    
#         print() 
# 

# num = int(input("Please enter the first number: "))

# while(num > 0):
#     for b in range(0, num):
#       b += 1
# print(b)  


# for i in range(len(numbers_list) - 2):
#         for j in range(i + 1, len(numbers_list) - 1):
#             for k in range(j + 1, len(numbers_list)):
#                 num1 = numbers_list[i]
#                 num2 = numbers_list[j]
#                 num3 = numbers_list[k]
                
#                 # Check if the sum is 100 and numbers are unique
#                 if num1 + num2 + num3 == 100 and len({num1, num2, num3}) == 3:
#                     return [num1, num2, num3]


# num = int(input("Please enter a number: "))

# armstrong_numbers = []
# number = 1

# while len(armstrong_numbers) < num:
#     sum_of_powers = 0
#     num_digits = number

#     digit = num_digits % 10
#     sum_of_powers += digit ** 3
#     num_digits //= 10

#     if number == sum_of_powers:
#         armstrong_numbers = armstrong_numbers + [number]
#     number += 1

# print(f"The first {num} Armstrong number: [{armstrong_numbers}]")

# num_digits for digit in num_str = num_str.split(",")

# import sys

# numbers = sys.argv[1:]

# print("Display all elements:")
# for number in numbers:
#     print(number, end=' ')
# print()

# print("\Elements in even positions: ")
# for i in range(len(numbers)):
#     numbers = [int(numbers) for arg in numbers]
#     average = sum(numbers) / len(numbers)
#     print(numbers[i], end=' ')
# print()

# import sys

# if len(sys.argv) < 2:
#     print("Usage: python program.py num1 num2 ...")
#     sys.exit(1)

# number = sys.argv[1:]
# numbers = [int(arg) for arg in number]
# average = sum(numbers) / len(numbers)

# print(f"Average of the numbers {numbers} is: {average}")


# from itertools import combinations

# def find_triplet_with_sum(numbers, target_sum):
#     # Generate all combinations of 3 numbers from the list
#     for triplet in combinations(numbers, 3):
#         if sum(triplet) == target_sum:
#             return triplet
#     return None

# # Input string containing numbers separated by commas
# input_string = input("Enter numbers separated by commas: ")

# # Convert input string to list of integers
# numbers = list(map(int, input_string.split(',')))

# # Target sum we want to achieve
# target_sum = 100

# # Find the triplet with sum equal to target_sum
# triplet = find_triplet_with_sum(numbers, target_sum)

# # Output the result
# if triplet:
#     print(f"A triplet with sum 100: {triplet}")
# else:
#     print("No triplet found with sum 100.")
# 

# Numb = input("Enter numbers separated by commas: ")

# numbers = Numb.split(",")
# targetSum = 100

# for i in range(len(numbers)):
#   for j in range(i + 1, len(numbers)):
#     for k in range(j + 1,len(numbers)):
#       num1 = numbers[i]
#       num2 = numbers[j]
#       num3 = numbers[k]

#       if num1 + num2 + num3 ==100 and len({num1, num2, num3}) == 3:
#         print(num1, ",", num2,",", num3)

# import sys

# cmdarguments = sys.argv [1:]
# print(cmdarguments)

# totalSum = 0
# for number in cmdarguments:
#     totalSum = totalSum + int(number)

# average = totalSum / len(cmdarguments)

# print(f"Average of the numbers is: {average:.2f}")

# count = 9
# print(1)
# for a in range(2,51):
#     isPrime =True
#     for i in range(2,a):
#         if(a%i==0):
#             isPrime = False
#             break
#     if(isPrime == True):
#         print(a,end=" ")
#         count = count - 1
#     if count == 0:
        # break

# count = 1
# while count <= 100:  
#   if(count % 3 == 0) and (count % 5 == 0):
#       print("FizzBuzz")
#   elif(count % 3 == 0):
#       print("Fizz", end = " ")
#   elif(count % 5 == 0):
#     # print("Buzz")
#     if(count == 25):
#       print(count)
#     else:
#       print("Buzz", end = " ")
#   else:
#     if(count == 50):
#       print(count)
#     else:
#       print(count, end = " ")
#   count += 1

# count = 1
# while count < 100:  
#     if(count % 3 == 0) and (count % 5 == 0):
#       print("FizzBuzz", end = " ")
#     elif(count % 3 == 0):
#       print("Fizz", end = " ")
#     elif(count % 5 == 0):
#       print("Buzz", end = " ")
#     else:
#         print(count, end = " ")
#     count += 1

# number = int(input("Enter an integer number:"))

# count = 0
# while count > 0:
#   if number % 2 == 0:
#     number /= 2
#     print(number, end = " ")
#   else:
#     number = (3*number) + 1
#     print(number, end = " ")
# count += 1
    # break

string = "abbcccccaaa"
count=0
newString = ""
for i in range(1, len(string)): 
    if string[i]==string[i-1]:
        count+=1
        if(i+1)==len(string):
            newString += string[i]+str(count+1)
    else:   
        newString += string[i-1]+str(count+1)           
        count=0        
print(newString)