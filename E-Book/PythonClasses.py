# 1
"""
# Main.py
from Person import Person

name = input("Enter name")
age = input("Enter age")

person = Person(name, age)
print("Person Details")
print(person.name)
print(person.age)

# Person.py

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
"""

#################################################################
# 2
"""
Main.py
from Person import Person

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)

Person.py

class Person:
	def __init__(self,name, age):
		self.__name = name
		self.__age = age
		
	@classmethod
	def from_string(cls, person_str):
		#fill your code
		name, age = person_str.split(",")
		return f"{name} is {age} years old"
		
	def __str__(self):
		#fill your code
		return f"{self.__name} is {self.__age} years old"
"""
	
