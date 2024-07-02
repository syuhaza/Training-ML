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

