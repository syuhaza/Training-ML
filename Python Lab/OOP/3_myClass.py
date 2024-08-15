# Encapsulation 
# Encapsilate the properties inside the class
# in other languages we have keywords public, private, protected
# to protect the properties

class circle:

    def __init__ (self, radius):
        # change  the property with single underscore
        # this make the property private
        self._radius = 0
        if(isinstance(radius, int)):
            self._radius = radius
        else:
            print("Invalid Radius")

    def area(self):
        return 3.14 * self._radius * self._radius
    
    def circumference(self):
        return 2 * 3.14 * self._radius
    
    def __str__(self):
        return f"Radius of this circle is {self._radius}"
    
mycircle = circle(20)
print(mycircle)
# mycircle = circle("abc")
# print(mycircle)
mycircle.radius = "abc"
print(mycircle)
print(mycircle.area())

#########################################################

class circle:

    def __init__ (self, radius):
        # change  the property with single underscore
        # this make the property private
        self.__radius = 0
        if(isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")
    #getter method and setter method
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if(isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # property is a class
    # we are calling /invoking the class  by passing the method as argument
    # Please notice after getRadius there is no ()
    # the propert class returns the property object which is assigned to
    # a variable radius
    # in other words radius is an instance of property class
    radius = property(getRadius, setRadius)
    
    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius
    
    def __str__(self):
        return f"Radius of this circle is {self.__radius}"
    
mycircle = circle(20)
print(mycircle)
# mycircle = circle("abc")
# print(mycircle)
# mycircle.__radius = "abc"

# you indirectly 
mycircle.radius = 30
print(mycircle)
print(mycircle.getRadius())
print(mycircle.area())
print(mycircle.circumference())

print(mycircle.setRadius(30))
print(mycircle.area())
print(mycircle.circumference())
print(mycircle.getRadius())







