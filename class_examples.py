import sys
import math
import random
import threading
import time

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    @property #getter definition starts with "property"
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter #setter definition has keyword setter in it
    def height(self,value):
        if value.isdigit():
            self.__height = value 
        else: 
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width = value 
        else: 
            print("Please only enter numbers for width")
    
#general methods available from the class
    def get_area(self):
        return int(self.__width) *int(self.__height)


square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())

class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight
    @property #getter
    
    def name(self, name):
        self.__name = name
    
    def make_noise(self):
        return "Grrrrr"
    
    def __str__(self):
        return "{} is a {} and says {} and weighs {} lbs".format(self.__name, type(self), self.make_noise(), self.__weight)
    
    def __gt__(self, animal2):
        if self.__weight > animal2.__weight:
            return True
        else:
            return False
        
#other magic methods
#__eq__ : Equal
#__ne__ : Not Equal
#__lt__ : Less Than
#__gt__: Greater Than or Equal 

#inheritcance
class Dog(Animal):
    def __init__(self, name="unknown", owner= "unknown", weight=0):
        Animal.__init__(self,name,weight)
        self.__owner = owner 

    def __str__(self):
        return super().__str__() + " and is owned by " + \
            self.__owner 


animal1 = Animal("monkey", 100)
print(animal1)

dog = Dog("Bowser","Bob", 150)
print(dog)

print(animal1 > dog)








