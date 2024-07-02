#Given number is 97531
#Want to reverse the number

a0 = 97531 
result = a0 % 10 #remainder
a1 = a0 // 10 #quotient
print(result, a1)

result = (result * 10) + (a1 % 10)
a2 = a1 // 10
print(result, a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result, a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result, a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result, a5)

givenNumber =  97531
result = 0 
result = givenNumber % 10 #1
# givenNumber = givenNumber // 10 #9753
givenNumber //= 10 #9753
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 #975
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 #97
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 #9
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 #0
result = result * 10 + (givenNumber % 10)


str_numbers = input()
str_numbers = str_numbers.split(",")
print(str_numbers)

numbers = [int(str_number) for str_number in str_numbers]
print(numbers)
numbers = map(int, str_numbers)
# print(list(numbers))
print(set(list(numbers)))

fruits = [{"Apple",10,}]
# tuple can be inside the set
# bcause both are hashable
# cant be modify
# but list cant be inside set

nestedlist = [
    [1,2,3],
    [3,4,5],
    [1,2,3]
]
nestedlist = [tuple(item) for item in nestedlist]
print(set(nestedlist))

