#RECURSION

#Factorial Example

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))

#DECORATORS - change inhance alter how the function works
# it is define with attherate symbol

def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("After")
        return val
    return wrapper


@logtime #so we have vhanged behaviour of the function without modifing the actual function
def hello():
    print("Hello")

hello()


#DOCSTRINGS - its a documentation of the function class file and everything in a project

class Dog:
    """A class representing a dog""" #This is how docstring is used in a class
    def __init__(self, name, age): #This is how docstring is used in a mehod
        """Initalize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("WOF!")

print(help(Dog)) #provides information