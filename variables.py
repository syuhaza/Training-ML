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

#in other programming language we called  these as variable initialization
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



