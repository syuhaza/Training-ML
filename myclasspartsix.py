# Polymophism

class Gender:
    def __init__(self):
        pass

    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry heavy object.")

class Female(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry Light object.")

def getGender(name):
    if "Binti" in name:
        return Female()
    else:
        return Male()

# python dynamically set the data type for the gender variable
# sometimes it becomes Male object
# sometimes it becomes Female object

gender = getGender("Syuhada Binti Zainal")
gender.doCarryObjects()
print(type(gender))

gender = getGender("Zainal Bin Raof")
gender.doCarryObjects()
print(type(gender))
