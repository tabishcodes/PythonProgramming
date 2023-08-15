#VARIABLE SCOPES
age = 10 #Global Variable - it can be access from anywhere in the specific file.

def test():
      age = 11 #Local Variable - it can only be access within a function.
      print(age) 

print(age)
test()


#NESTED FUNCTIONS - Function inside a Function

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ') #split is a way to create a list & the following split is spacing
    for word in words:
        say(word)

talk('I am going to buy the milk.')


def count():
     count = 1

     def increment():
          nonlocal count #nonlocal to access the variable in the parent function
          count = count + 1
          print(count) 
     increment()

count()


#CLOSURES

def counter():
     count = 0

     def increment():
          nonlocal count
          count = count + 1
          return count
     
     return increment

increment = counter() #way to call the inner function

print(increment())
print(increment())
print(increment())


#OBJECTS
#Everything in the python are objects
#Its as the attributes and methods that can be access using dot symbol

age = 8

print(age.real) #real value if any
print(age.imag) #imaginary value if any
print(age.bit_length()) #returns the number of bits required to represent an integer in binary notation, excluding the sign and leading zeros.

items = [1, 2]

items.append(3) 
items. pop()
print(id(items)) #prints the location in the memory

#LOOPS

#While Loop
condition = True

while condition == True: #if the condition is true they it will run
    print("Its's True") #but in this casr it will be running infinite time
    condition = False #this will stop the loop as the condition is False now
#Mostly copunter are used to stop the While Loop

#For Example
count = 10

while count >= 0:
     print("Coundown Started !!!")
     print(count)
     count -= 1

print("Boom !!!")

#For Loop
items = [1, 2, 3, 4, 5]

for item in items:
     print(item)

#Range Fumctiom

for item in range(10):
     print(item)

#Enumerate Function - It will return each item with index
for index, item in enumerate(items):
     print(index, item)


#BREAK & CONTINUE
#used between loops to interup

item = [1, 2, 3, 4, 5]
#Continue Function
for item in items:
     if item == 2:
          continue #its skips the iteration in loop 
     print(item)
#Break Function
for item in items:
     if item == 2:
          break #its altogether break the iteration in all the loop 
     print(item)