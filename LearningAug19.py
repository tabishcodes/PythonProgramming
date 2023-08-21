#THIRD PARTY PACKAGES 

#HOW TO INSTALL THIRD PARTY PAKAGES USING PIP
# 1) GO TO THE TERMINAL
# 2) Syntax TO install a package - pip install <PACKAGE NAME>
# 3) Syntax TO upgrade a package - pip install -U <PACKAGE NAME>
# 4) Syntax TO install a package specific version - pip install <PACKAGE NAME>==<VERSION>
# 5) Syntax TO uninstall a package - pip uninstall <PACKAGE NAME>
# 6) Syntax TO know about a package - pip show <PACKAGE NAME>


#LIST COMPRESSIONS - advance topic on list

numbers = [1,2,3,4,5]

numberPower2 = [n**2 for n in numbers]

print(numberPower2)

#List Compression with a loop

numberPower2 = []
for n in numbers:
    numberPower2.append(n**2)

print(numberPower2)


#POLYMORPHISM

class Dog:
    def eat(self):
        print("Eat dog food.")

class Cat:
    def eat(self):
        print("Eat cat food.")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#OPERATOR OVERLOADING

class Dog:

    def __init__(self, name, age : int): 
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False

roger =  Dog('Roger', 6)
tommy = Dog('Tommy', 3)

print(roger < tommy)

