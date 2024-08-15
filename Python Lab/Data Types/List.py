# 4 different type builtin data structure
#list, tuple, set, dictionary

# list uses []
# list is modified (append, edit, delete)
# list is ordered (the items retain its position)
# indexed (0,1,2,3,4,5,....)
# allow duplicates

fruits= ["apple","orange","mango","banana","grape"]
# fruits is a variable assigned with multiple values
# fruits is also called an object
# if anything is called as object, which means it is instance of a class
# Jegan, Peter are object, instance of Human class
# Properties = eyes (2), nose (1)
# Method = walk, run, eat
print(fruits)

#Refer to variableparttwo.py

#MOdifiable
fruits.append("durian")
print(fruits)
 
fruits.insert(1,"rambutan")
print(fruits)

fruits.insert(3,"cempedak")
print(fruits)

# update item in the list

fruits[5] = "mangosteen"
print(fruits)

fruits.remove("durian")
print(fruits)

fruits.pop()
print(fruits)

# delete an item by index
# we can delete anything from memory permantly using the keyword del

greeting = "Good Morning"
del greeting
# print(greeting) NameError
# print([1,2,4,5]  + 5) =atypeError
del fruits[3]
print(fruits)

fruits.clear()
print(fruits)

del fruits #this will delete the entire list
#print(fruits)

fruits= ["apple","orange","mango","banana","grapes", "apple", "mango"]
print(fruits.index("mango")) # 0,1

newFruits = fruits[2:] # 0,1
print(fruits.index("mango")+1)
# Enumerate return list of tuple
print(list(enumerate(fruits)))
# Each tuples have 2 items, the first item is the index and the second item ist the fruit
for item in enumerate(fruits):
    if item[1] == "mango":
        #print(item[0])
        #print(item[1])
        print("Mango is in position:", item[0])

print("Total number of apples:", fruits.count("apple"))

# Sort the items in the list
# alphabet ascending
fruits.sort()
print(fruits)

#reverse
#alphabet descending
fruits.reverse()
print(fruits)

#print downward
for fruit in fruits:
    print(fruit)


# fruits.copy()
x = [10,20,30,40,50]
y = x
print(x)
print(y,"\n")
x[2]= 35
print(x)
print(y)


# perform deep copy
x = [10,20,30,40,50]
# y = x Dont do this
y = []
for i in x:
    y.append(i)
print("="*40)
print(x)
print(y,"\n")
x[2]= 35
print(x)
print(y)

# Infact you dont need to create a for loop to copy
# rather you can just you copy method
x = [10,20,30,40,50]
# y = x Dont do this
y = x.copy()
print("="*40)
print(x)
print(y,"\n")
x[2]= 35
print(x)
print(y)

# ford-fulkerson algorithm
# floyd warshall algorithm

# fruit is an instance of a list class
# Technically the object are created by calling the class
x = list([15,25,35,45,55])
print(x)
# however in python to create list instead of using class they let use []
x = [15,25,35,45,55]
print(x)

# In python  to invoke / call the operator the function use () parenthesis 
# to call built in function print() sum() id()
# To create object we call the class type() int() float() list()
# To call function inside a module sys.path()
# To call method in a object "Television".split()

def total(numbers):
    result = 0
    numbers[2]=35
    for number in numbers:
        result = result + number
    return result

x = [10,20,30,40,50]
print(x)
print(total(x))
print(x)
#convert list to tuple
# you pass the list 
x = tuple(x)
# print(total(x))


fruits = ["apple","orange","mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]

fruit01,fruit02,fruit03 = fruits

