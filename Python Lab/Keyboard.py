#python has built in function that called input

# firstnumber = input("Please enter first number: ")
# print(firstnumber)

# secondnumber = input("Please enter second number: ")
# print(secondnumber)
# #the input is always return value of type string
# print(type(firstnumber))

# secondnumber = input("Please key in the second number")
# print(firstnumber + secondnumber) #string concatenation
# print(int(firstnumber) + int(secondnumber)) #addition

numbers = input("Enter the numbers to di Total:")
numberlist = numbers.split(",")
print(numberlist)
total = 0
for number in numberlist:
    #int function trim the string value
    #remove the spaces in the string and then convert
    #string to integer
    total = total + int(number)
print(total)