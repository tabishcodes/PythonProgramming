#HAPPY INDEPENDENCE DAY

#CLASSES

#An Object is an Instance of a class
#A class is a type of an object

#Inheritance
class Animal():
    def walk(self):
        print("Walking!")

class Dog(Animal): #now the dog class will inherit from the animal class
    def __init__(self, name, age): #its a constructor; used within the a class; called when object is created from a class; 
        self.name = name
        self.age = age

    def Bark(self):
        print("Woof!")

roger = Dog("Tommy", 7)

print(type(roger))

print(roger.name)
print(roger.age)

roger.Bark()
roger.walk()

#MODULES

#Every python file is a module
#Modules can be imported from other files

#import module/file to the existing file so that we can use every classes, functions, etc.
import LearningAug14 
LearningAug14.bark() #calling a function from other files

#using from function to import we are using the specific function from a file
from LearningAug14 import bark 
bark()

#We can also call modules if its in the sub folder
from lib import dog
dog.bark()

#specific function call from sub folder
from lib.dog import bark
bark()

#Standard Libraries used in python
import math
print(math.sqrt(4))

#we can also import specific functions from math library
from math import sqrt
print(sqrt(16))