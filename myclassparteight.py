# in every class there will be many properties
# and very fews properties are  common to all the objects
# its good to keep these properties as the class level
# rather than keep these properties at the class level
class Participant:
    course = "Python Data Science / Machine Learning"

    def __init__(self, firstname, lastname):

        self.firstname = firstname
        self.lastname = lastname
        count = 1
        print(self.firstname, self.lastname, count)

    def getFullName(self, firstname, lastname):
        print(self.firstname, self.lastname)
        