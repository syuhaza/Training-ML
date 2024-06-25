# FUnctions are to organize our code
# FUnctions are not for solving like operators, if, for, while
# Let say you want to copy this line & paste it in 5 places
# thne it must converted to a function

def sayHelloWorld():
    print("Hello World inside the function!!!")

# Function are created by using the keyword 'def'
# followed by function name
# followed by parathensis ()
# followed by colon :
# block of code inside the function with indentation

sayHelloWorld()

# if that function takes some value
# must create a variable (placeholder) in between the bracket
# if more than 1 value
# create more than 1 variable(s) (placeholder) separated by comma
# these variable/variables called "parameter"

def greeting(name):#parameter inside ()
    print("Good Morning", name)

# when call the functio, must pass value to the parameter
# the value we are passing is argument
# the number of argument(s) must match with number of parameter(s)

greeting("Nursyuhada")

def total(x, y, z):
    result = x + y + z
    print("Result:", result)

total(10, 20, 40)



def buyLunch(makan, minum):
    prices = [] #empty list
    for food in makan:
        if food == "nasi":
            prices.append(2.80)
        elif food == "sayur":
            prices.append(2.20)
    for drink in minum:
        if drink == "nescafe":
            prices.append(2.50)
    return prices

itemprices = buyLunch(["nasi", "sayur"],["nescafe"])
total = 0
for price in itemprices:
    total += price
print("Amount to be paid:", total)

#whther the return value must a be a list
def simpleInterest(principal, period, rate):
    interest = (principal* period *rate) / 100
    # return [interest, principal, period, rate]
    return interest
print("Interest Amount:",  simpleInterest(1000, 1, 6))

# when you return more than one value separated by comma
# it will be a tule (tuple is nothing but read only list)

def participantsList(nameone, nametwo, namethree):
    nameone = nameone + "Data Science"
    nametwo = nametwo + "Data Science"
    namethree = namethree + "Data Science"
    return nameone, nametwo, namethree
result = participantsList("John ", "Peter ","Parker ")
print(type(result))
print(result)

def calculatesimpleInterest(principal, period=1, rate=6):
    interest = (principal* period *rate) / 100
    # return [interest, principal, period, rate]
    return interest

#not passing the value of rate parameter
#the rate automatically become 6
print(calculatesimpleInterest(1000,2))

# is there way to pass values for principal and rate only
# called "Named Argument"
# the name is referring to parameter
print(calculatesimpleInterest(principal=1000,rate=5))

# can declare the parameter to be able 

def calculateTotal(*givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total += givenNumber
    return total

# Variable length Argument
# the number of arguments which we pass varry
# caller can pass the values as a list
print(calculateTotal(10,20,30))
print(calculateTotal(10,20,30,40,50,60))
print(calculateTotal(10,20,30,40,50,60,70,80,90))

def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit) == 6: print(fruit)

#we are sending the itmes/fruits induvidually (not as a list)
#however python will convert them to a list of fruits and pass it
listSixLetterFruits("apple","orange","mango","banana","durian","grapes")


def listSixLetterFruits(*fruits):
    for fruit in fruits:
        print(fruit)

#we are sending the itmes/fruits induvidually (not as a list)
#however python will convert them to a list of fruits and pass it
listSixLetterFruits("apple",20, 1.40,"orange",4, 1.20)

def listSixLetterFruits(*fruits):
    for fruit in fruits:
        print(fruit)

listSixLetterFruits("apple",20,1.40,"orange",40,1.20)

def sum(a,b):
    return a + b
print(sum(10,20))

# reminder when we see "function(value)" we always call values as argument
# in the above statement it looks we are passing

def minus(a,b):
    return a - b

"""def arithematic(keyword, a, b):
    if keyword == "s":
        return sum(a,b)
    elif keyword == "m":
        return minus(a,b)
"""
# arithematic("s", 10, 20)
# notice no there is no () after the function name
# this is how you pass function as an argument to another 
def arithematic(func, a, b):
    func(a,b)
    
arithematic(minus, 10, 20)
arithematic(sum, 10, 20)

def mul(a,b):
    return a * b