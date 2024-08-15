# Is - A Realtionship 
# Alumni is a student
class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

    def __str__(self) -> str:
        message = f"Firstname = {self.firstname}\n"
        message += f"Lastname = {self.lastname}\n"
        message += f"IC number = {self.icnumber}"
        return message
# Alumni extends Student class
class Alumni(Student):
    #     # calling the __init__ method statically 
    #     # student.__init__(self, firstname, lastname)
    #     # To create the parent object of parent class
    #     # To create the parent object inside the child object
    #     # YOU CAN USE SUPER CLASS
    #     # WHICH WILL RETURN the object of parent class
    def __init__(self, firstname, lastname, graduation, degree):
        super().__init__(firstname, lastname)
        self.icnumber = ""
        self.graduation = graduation
        self.degree = degree

    def __str__(self):
        message = f"Firstname = {self.firstname}\n"
        message += f"Lastname = {self.lastname}\n"
        message += f"IC number = {self.icnumber}\n"
        message += f"Graduation date = {self.graduation}\n"
        message += f"Degree course = {self.degree}"
        return message

# we have create and object of Alumni class
alumni = Alumni("Shu","Shi",2024,"AI")
student = Student("Shu","Shi")
# alumni = Alumni()
print(alumni)
print("-"*100)
print(student)