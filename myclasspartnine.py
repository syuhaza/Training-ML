class calculator:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    

mycalculator = calculator(20, 10)
print(mycalculator.add())
print(mycalculator.subtract())

class Utility:

    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
