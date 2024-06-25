#So far we have learn how to assign single value to single variable
#multiple values to multiple variable
#x = 10
#x, y = 10, 11

#Learn how to assign multiple values to a single variable.
#New data structure called "List"
#In other programming called 'Array'

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

