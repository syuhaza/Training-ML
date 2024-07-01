class Passport:

    def __init__(self, country, passportNumber):
        self.country = country
        self.passportNumber = passportNumber


class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = ""