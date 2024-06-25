#String concatenation (+) both string
firstName = "Khairi"
surName = "Abu Bakar"
fullname = firstName + surName
print(fullname)

carPlate = "JCG"
number = 6574
carPlateNumber = carPlate + str(number)
print(carPlateNumber)

product = "toma"
print(product * 50)

#so far we know strings are enclosed with double quote
#or single quote
#we can usee triple quote
#traditionally multiline
#\n = new line
#\t = tab 
#\r = carriage return
message = "As I am not feeling well\n"
message = message + "I wont be able to attend the \tmeeting.\n"
message = message + "Please proceed...\n"
print(message)

myfile = "c:\newfolder\table\read.txt"
print(myfile)
#double slash
myfile = "c:\\newfolder\\table\\read.txt"
print(myfile)
#special character = r
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

message = """As I am not feeling well
I wont be able to attend the meeting
Please proceed..."""
print(message)

#relationship between string and list
#strings are nothing but list of character
mygreetings = "Hello World"
print(mygreetings[0])
print(mygreetings[0:6])
print(mygreetings[::2])
print(mygreetings[::-1])
#how many character 
print(len(mygreetings))

#reverse the given number
givennumber = 12345
print(int(str(givennumber)[::-1]))

#when i started this python class
#"Television" is a string literal / string value
#"Television" is also called string object
product = "Television Cloths Vegetables"
print(product.split()) #split function takes the literal
#product and split them ot tokenize them into multiple words
#using space as separator 
#list of words
#Functions inside the object is also called "Method"
#from now you must say "print is a function"
#where as "split is a method"

