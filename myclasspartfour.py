class Passport:

    def __init__(self, country, passportNumber):
        self.country = country
        self.passportNumber = passportNumber

    def __str__(self):
        return f"Country: {self.country} \nPassport Number: {self.passportNumber}"


class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Customer has a passport
        # When you have a
        self.icnumber = ""
        self.passport = None

    def __str__(self):
        message = f"First Name: {self.firstname}\n"
        message = message + f"Last Name: {self.lastname}\n"
        message = message + f"IC Number: {self.icnumber}\n"
        if (self.passport != None):
            message = message + self.passport.__str__()
        return message

peter = Customer("Parker","Peter")
passport = Passport("UK","E0202932")
peter.passport = passport
print(peter)
print(peter.__dict__)