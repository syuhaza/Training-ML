# principle = 1000
# period = 1
# rate = 6
# simpleInterest = (principle * period * rate) /100
# print("Simple Interest:", simpleInterest)

"""
def calculateSimpleInterest(principle, period, rate):
    simpleInterest = (principle * period * rate) /100
    return simpleInterest

def calculateTotalAmount(principle, simpleInterest):
    return principle + simpleInterest


principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest(principle, period, rate)
newResult = calculateTotalAmount(principle,result)

print("Simple Interest:", result)
print("Total amount to be paid:", newResult)

"""

# 
class Student:

    # 1) Method is nothing but a function that inside a class
    # 2) Method atleast 1 parameter
    # 3) 
    def __init__(self):
        print("Object is created")

    # This is our first method/function inside the class student
    # remember methods must have atleast 1 parameter
    def attendClass(self):
        print("Object started attending the class")
    
    def doProject(self, projectname):
        print("Object started doing the project:", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtained the score {grade}"

# Let us create our first object
syuhada  = Student()
syuhada.attendClass()
syuhada.doProject("Pokemon")
syuhada.attendExam("Python 1")