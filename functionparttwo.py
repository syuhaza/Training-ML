# function can have inner function
def sum (a,b):
    return a + b

x = 10

# Annonymous function assigned to a variable
# sum = def (a,b):
#      return a + b

# Outer function
def aunthecating(username,password):
    # we have created an inner function
    def calculateSI(principle, period, rate):
        result = (principle*period*rate) / 100
        return result
    if username == "admin" and password == "pwd123":
        # since calculateSI function is inside the aunthencate function
        # we can call this function here
        # print("Simple Interest: ",calculateSI(1000, 1, 6))
        #instead of calling calculateSI
        return calculateSI

# if you can call the function which is in this context
# authenticate("admin","pwd123")
# you cannot call the function which is inside another function content
# calculatesi(1000, 1, 6)

func = aunthecating("admin","pwd123")
print("Simple Interest: ", func(1000, 1, 6))

                                # Outer function        # Inner Function                                                                                                                                                                                                                                                                                    
print("Simple Interest: ", aunthecating("admin","pwd123")  (1000, 1, 6))


# Annonymous function means function without name
# however if you create function without a name how to call them?
# So it is always good to assign the annonymous function to a variable
# sum = def (a,b):
    # return a + b
# The above is not a valid syntax in python, however this is every functions are
# handled by python itself
# That means in python every function is an annonymous function

# In python theu do have landa function which let you to create function in 1 line
# the function can have only one statement (line of code)
# def add(a,b): return a + b
# let us create a lambda function(is also annonymous function)
# add = def(a,b): return a + b
# Instead of def use lambda and donot use return
add = lambda a,b: a + b

fahrenheitvalues = [32,33,34,35,36,38,40]
def fahrenheitTocelcius(fahrenheitvalues):
    return (fahrenheitvalues - 32)* 5/9

celciusvalues = map(fahrenheitTocelcius, fahrenheitvalues)
print(list(celciusvalues))

# Using lambda function
""" 
Step 1: create a annonymous function
def fahrenheitTocelcius: return (fahrenheitvalues - 32)* 5/9 

Step 2: assign it to variable
fahrenheitTocelcius = def (fahrenheitvalues): return (fahrenheitvalues - 32)* 5/9 

Step 3: rename def to lambda
fahrenheitTocelcius = lambda (fahrenheitvalues): return (fahrenheitvalues - 32)* 5/9 

Step 4: remove () at parameter and return keyword
fahrenheitTocelcius = lambda fahrenheitvalues: (fahrenheitvalues - 32)* 5/9 
"""

celciusvalues = map(fahrenheitTocelcius, lambda value: (value -32) * 5/9)
print(list(celciusvalues))
