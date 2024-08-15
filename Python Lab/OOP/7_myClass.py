# Multiple inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print('Inside the card')

class ATM(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print('Inside the ATMcard class')

class creditCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print('Inside the Creditcard class')

class debitCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print('Inside the Debitcard class')

class BankCard(ATM, creditCard, debitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print('Inside the Bankcard class')
        super().doSomething()

# we have created 5 classes
# let us create instance of the last card

bankCard = BankCard()
bankCard.doSomething()
# it call the super().something
# this time the ATM class will be called ()

# python scan from left to right and identify the base class
# and calls the methods accordingly
# this process called Method Resolution Order (mro)
print(BankCard.__mro__) # to show the process of calling the method

# <class '__main__.BankCard'>
# <class '__main__.ATM'>
# <class '__main__.creditCard'>
# <class '__main__.debitCard'>
# <class '__main__.Card'>
# <class 'object'>

"""
BIGGEST CONCLUSION
Every class we create in python is inherited from a class called object

class object:
    def __init__():
        pass
    def __str__():
        return memory address
"""

class Student():
    def __str__(self):
        return "Student"

class Alumni(Student):
    def __str__(self):
        return "Alumni"

alumni = Alumni()
print(alumni)