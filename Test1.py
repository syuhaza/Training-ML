# num = int(input("Please enter a 2-digit number: "))

# givenNumber =  97351
# result = 0 
# result = givenNumber % 10 #1
# givenNumber = givenNumber // 10 #9753
# givenNumber //= 10 #9753
# result = result * 10 + (givenNumber % 10)
# print(result)
# num = 12
# r2 = num ** 2
 
# result = num % 10
# num //= 10
# result = result * 10 +(num%10)
# print(result)
# print(r2)
# result2 = r2 % 10
# r2 //= 10
# result2 = result2 * 10 +(r2%10)
# r2 //= 10
# result2 = result2 * 10 +(r2%10)
# print(result2)

# x = 0b10101100
# y = 0b11011001

# lower_x = x & 0b01011111
# cleared_x = x & 0b01011111
# print(bin(lower_x))
# print("Y is even number") if (y % 2 == 0) else print("Y is odd number")
# print(bin(cleared_x))

x = 0b10101100
y = 0b11010010

# Swap values without using a temporary variable
x = x ^ y
y = x ^ y
x = x ^ y

# Toggle 3rd and 5th bits of x
x = x ^ (1 << 2)  # Toggle 3rd bit
x = x ^ (1 << 4)  # Toggle 5th bit

# Check if two given numbers are different
a = 29
b = 15
are_different = a != b

# Print results
print("After swapping, x =", bin(x))
print("After swapping, y =", bin(y))
print("After toggling 3rd and 5th bits of x, x =", bin(x))
print("Are the numbers a and b different?", are_different)