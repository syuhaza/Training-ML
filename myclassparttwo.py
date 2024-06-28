class Student:

    # 1) Method is nothing but a function that inside a class
    # 2) Method atleast 1 parameter
    # 3) 
    def __init__(self,firstname,lastname,icnumber):
        # 1) Properties are nothing but variable but inside the class
        # 2) properties are always prefix by the first parameter
        # 

        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""

    def attendClass(self):
        print(f"{self.firstname} {self.lastname} started attending the class")
    
    def doProject(self, projectname):
        print(f"{self.firstname} {self.lastname} started doing the project:", projectname)

    def attendExam(self, exam):
        grade = "A+"
        return f"""{self.firstname} {self.lastname} has attended the exam: {exam} and obtained the score {grade}"""
    
    def info(self):
        print("First Name: ", self.firstname)
        print("Last Name: ", self.lastname)
        print("IC Number: ", self.icnumber)
        # Here the program is a local variable created inside the method
        for program in self.program:
            print("Program: ", program)
        print("Address: ")
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Postcode"])
        print(self.address["State"])
        print(self.address["Country"])

    def __str__(self):
        return f"""
        First Name: {self.firstname}
        Last Name: {self.lastname}
        IC Number: {self.icnumber}"""
        # Here the program is a local variable created inside the method
        for program in self.program:
            print("Program: ", program)
        print("Address: ")
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Postcode"])
        print(self.address["State"])
        print(self.address["Country"])
        

syuhada  = Student("Nursyuhada","Zainal", "000105080044")
syuhada.attendClass()#
syuhada.doProject("Pokemon")#
print(syuhada.attendExam("Machine Learning"))#
syuhada.program = ["Machine Learning", "Deep Learning", "Python"]
syuhada.address = {
    "Street":"52 Jalan WM 3A/4",
    "Area":"Behrang Stesen",
    "Postcode":35950,
    "State":"Perak",
    "Country":"Malaysia"
}
syuhada.info()

print(syuhada)