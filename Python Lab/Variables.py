product = "Television"
quantity = 5
price = 1455.25
available = True 

print("Product: ", product)
print("Quantity: ", quantity)
print("Price: ", price)
print("Available: ", available)
print(" ")
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

Total = quantity * price
print("Total: ", Total)

quantity = "10"
print(type(quantity))

total = int(quantity) * float(price)
print(total)


x = 100
print(x)
print(id(x))

a = "Hello"
b = "Hello"
print(id(a))
print(id(b))

#Assign more then one value to more than one variable
#In one line of statement

x, y =  102, 103
x, y =  102 + 1, 103 + 1
x, y =  x + 1, y + 1
print(x, y)

#In some programming language, you can assign multiple variables with single value
# x , y = 501 , however in python this is not allowed.

# In other programming language we called  these as variable initialization
# In python for you to create a variable without a assign a value
y = 0 #numeric initialization
y = " " #string initialization / empty string
y = None #keyword
#Keyword: True, False,None
print(type(y))

#keyword cannot be a variables

#Comparison Operators
myheight = 5.2
yourheight = 5.3
mysisterheight = 5.2

#Let us create True statement
print(yourheight > myheight) #greater than
print(myheight == mysisterheight) #equals to
print(mysisterheight < yourheight) #less than
print(myheight != yourheight) #not equals to

print(yourheight >= myheight) #greater than or equals to
print(myheight >= mysisterheight) #greater than or equals to

a = 21
b = 14
c = 7

print(a > b and a > c) #a is the greatest number
print(c < a and c < b) #c is the smallest number
print((b > c and b < a) or (b > a and b < c))

#Negation Operator
print(not (a > c)) #False
print(not (a < c)) #True

#Truth table
#XOR ^
print("XOR",(a > c) ^ (a > b))

########################################################################################################
""" Part two

So far we have learn how to assign:
* single value to single variable
* multiple values to multiple variable
x = 10
x, y = 10, 11

Learn how to assign multiple values to a single variable.
New data structure called "List"
In other programming it called 'Array' 
"""

fruit01, fruit02 = "Apple", "Orange"
fruits = ["apple", "orange", "banana", "grapes","mango"]

#indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

#how many items are there in the list
#there in built in function len
print("Number of items we have: ",len(fruits))

#how to find maximum index
print("Maximum index: ",len(fruits) - 1)

#does the index has to be positive?
#nit necessary it can be negative number (only in python)
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
#This also enables us to retrieve values in reverse

#Range start_index:end_index
#In python when we refer to Range the end_index is not included
print(fruits[1:3])
print(fruits[1:4])
#what if we did not mention the start index
print(fruits[:4])
#It will start index as 0

print(fruits[1:])
#It will until last index


fruits = ["apple","rambutan","orange","durian","banana","cempedak","mangosteen","grapes","mango"]
print(fruits[0:9])

#However I dont want all the items, step up index
print(fruits[0:9:2])
print(fruits[0:9:3]) #this feature is very important for us to take samples
#for example lets say we have 1 million records
#dont need to take all the data and process it
#want to take sample only 50 data
#and selection must be evenly distributed then we can use step up argument

#in the range also you can have negative numbers
print(fruits[-5:-1]) #position -1 has mango it is not included
print(fruits[-1:-5])
print(fruits[-1:-5:-1])#over here item at -5 is not included

print(fruits[::-1])#if you want to reverse the entire list

