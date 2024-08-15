"""
*Object Oriented Programming*

object - instance of a class

Class - blue print
class - 
	characteristic/data member/state
	functionalities/member function/behaviour
class Person
"""
class Person:
    first_name = "" # Public class variable
    __ic_number ="" # Private class variable

    def setIcNumber(number): # Public class method
        Person.__ic_number = number # Access private class variable
    def getIcNumber():
        return Person.__ic_number

Person.first_name = "Michael" # Access class variables
print(Person.first_name)      # Access class methods
Person.setIcNumber(983484)
print(Person.getIcNumber())   