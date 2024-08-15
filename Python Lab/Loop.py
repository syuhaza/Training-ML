#Whenever you want to iterate s list of items you must use for loop
fruits = ["apple","rambutan","orange","durian","banana","cempedak","mangosteen","grapes","mango"]
for fruit in fruits: #fruit is a temporary variable
    print(fruit)
#print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

#prints only fruits with 5 letters
for fruit in fruits:
    if(len(fruit) == 5):
        print(fruit)

#print fruit together with the index (position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1

#want to create a multiplication table of 5
#want to go until 12
#exp: 1 x 5 = 5

multipliers = [1,2,3,4,5,6,7,8,9,10,11,12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier,"x",multiplicant,"=",multiplier * multiplicant)

#however this is not practical when the until is 200 instead of 12
#we have to go for range option star_index:end_index
#but the : operator can work only an array
#we have a built in function called range which can generate numbers between them

#start index included and end index is excluded
print(range(1, 12))

print(list(range(1, 12)))

#let us do the multiplication table using range
multiplicant = 6
for multiplier in range(1, 13):
    print(multiplier,"x",multiplicant,"=",multiplier * multiplicant)

#split the digits in the input number and print them
#since we dont have it as a list & dont know the number of digits
#we have to use while loop
givennumber = 97409
while (givennumber > 0):
    print(givennumber % 10)
    givennumber //= 10

givennumber = 12345
numberofdigit = len(str(givennumber)) - 1
while (givennumber > 0):
    print(givennumber // 10 ** numberofdigit)
    givennumber %= 10 ** numberofdigit
    numberofdigit -= 1

givennumber = 67891
strGivenNumber = str(givennumber)
for digit in strGivenNumber:
    print(digit)



multiplicant = 6
multiplier = 1
for multiplier in range(1, 13):
# while(multiplier <= 12):
    print(multiplier,"x",multiplicant,"=",multiplier * multiplicant)
    multiplier += 1
    #jumps out of the loop (condition not fail yet 11 <= 12 true)
    #the code in the else block not executes.
    if multiplier == 11:break
else:
    print("Multiplication table done")


multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    if multiplier % 5 == 0: continue
    #what continue do is
    # whithout executing the following line(s) it will jump back to the loop
    print(multiplier,"x",multiplicant,"=",multiplier * multiplicant)
    
