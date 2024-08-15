# is nothing but read only list 
# tuple uses []
# tuple is not modifiable (cannot append, edit, delete)
# tuple is ordered (the items retain its position)
# indexed (0,1,2,3,4,5,....)
# allow duplicates

x = (10,20,30,40,50)
print(x)
print(type(x))

fruits = ("apple","orange","apple","mango")
print(fruits.count("apple"))
# not modifiable
# dont have append, insert, remove
# can delete the entire tuple using del keyword
del x

fruits = ("apple","orange","apple","mango")
print(fruits.count("apple"))

# tuple is doesnt have many features as list
# 1) take less space
# 2) faster than list

def returnFruits():
    # return keyword cannot return more than one value
    # so python
    return "apple", "orange"
print(type(returnFruits()))

def total(*numbers):
    print(type(numbers))
    result = 0
    for number in numbers:
        result = result + number
    return result
print(total(10,20,30,40,50,60))

# one last feature in tuple
#tuple can auto explode

fruits = ("apple","orange","mango")
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]

fruit01,fruit02,fruit03 = fruits
# we are assigning multiples items in the tuple  to multiple variables

x = (10)
# () is expression
# now python are confused it is tuple or expression
# python gives priority for expression than tuple
# automatically 10 (integer) is assigned to x
print(type(x))

x = (10,)
print(type(x))
