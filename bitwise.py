#how to represent binary numbers in python
#can use 0b followed by the binary number
#how ever it is still an integer
ownerpermission = 0b111 #0b convert into binary. Its start reading it as one one one
#instead of one hundred and eleven
print(ownerpermission)

filepermission = 0b111101001 
#now owner can read, write and execute
#group can read and execute
#others can execute only

#in data science/machine learning when you are given
#categorical data you must convert them to numbers
#which machine can understand
#this itself called "feature engineering"
#gender representation 01 for female and 10 for male

#this bit extraction can be using bitwise adn operator
mask = 0b000111000
# print("{0:b}".format((filepermission & mask) >> 3)) #answer in binary
print(format((filepermission & mask) >> 3)) #answer in dec

#in order to perform n=bit extraction we use bitwise & operator
#we are interested in 4, 5, 6 bits only
#AND
#Original data              111101001   &
#Our mask                   000111000
#4,5,6 bits extracted       000101000
#shift it to right 3 times  000000101 >> 3
# & used to extract the data
print(bin(filepermission & mask)) 

#OR
#Original data              111101001   |
#Our mask                   000111000
#4,5,6 bits extracted       111111001
#The or operator is used to set a specific bit to 1
#Please remember there is no way to set a specific bit to 0 using or operator
#Or operator is also used in extracting region of the image
print(bin(filepermission | mask)) 

#XOR
#Original data              111101001   ^
#Our mask                   000111000
#4,5,6 bits extracted       111010001 
#xor is used for encryption
message = 0b01001010 # my content "J"
key = 0b00101100 # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))

decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))

#1st complement
givennumber = 5
#5          0101
#1s compliment 1010
#2s compliment = 1s compliment + 1
print(~givennumber + 1) #~ 1s compliment
print(-givennumber) #- unary negative
print(+givennumber) #+ unary positive

#hash

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A,   B,  C,  D, E, F
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14
hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 13, 14, 15
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14

octadecimalnumber = 0o10
print(octadecimalnumber)
print(oct(octadecimalnumber))