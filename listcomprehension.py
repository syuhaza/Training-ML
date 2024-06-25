#deep copy
fruits = ["apple", "orange","mango","banana","grapes"]
prices = [1.60,2.30,4.50,3.10,1.40]

# for loop with some statement
for fruit in fruits:
    print(fruit)

# overseafruits = fruits #you shouln't actually do this
# overseafruits = fruits.copy()

overseafruits = []
#for loop with list
for fruit in fruits:
    overseafruits.append(fruit)

# use list comprehension
overseafruits = [fruit for fruit in fruits]
print(overseafruits)

# use tuple comprehension
overseafruits = (fruit for fruit in fruits)
print(overseafruits)

priceswithsst = []
for price in prices:
    pricewithsst = price + (price * 0.06)
    priceswithsst.append(pricewithsst)

# use list comprehension
priceswithsst = [price + (price * 0.06) for price in prices]
print(priceswithsst)

def calculateSST(price):
    pricewithsst = price + (price*0.06)
    return pricewithsst

priceswithsst = map(calculateSST, prices)

fahrenheitvalues = [32,33,34,35,36,38,40]
celsiusvalue = []
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalues = (fahrenheitvalue - 32)* 5/9
    celsiusvalue.append(celsiusvalues)


# celsiusvalues =  map(fahrenheitvalues)
# all the three above examples are trying to create a new list
# The number of items in both list are same
# instead of writing the traditionally for loop
# you can use something called list comprehension or filter class


multiplesofthree = []
for number in range(1,50):
    if(number % 3 == 0):
        multiplesofthree.append(number)

# map and filter are class
# use list comprehension
multiplesofthree = [number for number in range(1,50) if(number % 3 == 0)]
print(multiplesofthree)

def findMultiplesOfThree(number):
    return True if (number % 3 == 0) else False

multiplesofthree = filter(findMultiplesOfThree, range(1,50))
print(list(multiplesofthree))

numbers = [2,3,5,4,22,11,6,9,43]
oddnumbers = []
for number in numbers:
    if (number % 2 != 0):
        oddnumbers.append(number)

def isOddNumber(number):
    return True if (number % 2 != 0) else False

oddnumbers = filter(isOddNumber, numbers)
print(list(oddnumbers))

# use list comprehension
oddnumbers = [number for number in numbers if(number % 2 != 0)]

# cannot use list comprehension
sum = 0
for number in range(1,11):
    sum = sum + number
print("Sum: ",sum)


mean = 0
for number in range(1,11):
    mean = mean + number
mean = mean / len(range(1,11))
print("Mean: ",mean)
# In the above three examples we are reduce the value into a single value

# reduce is not a built in function
# it is inside a module called itertools

from functools import reduce
# reduce()

numbers = [1,2,3]

def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue

reduce(findTotal, numbers)

# reduce function takes another function as first parameter
# that function suppose to take 2 parameter
# reduce function takes list as second parameter
"""def reduce(func, numbers):
    sum = 0
    # however the original reduce function is smart
    #it will initialize the sum variable with 1 if you use multiplication
    for number in numbers:
        sum = func(sum, number)
    return sum"""

def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))
print(reduce(factorial, numbers, 5))



