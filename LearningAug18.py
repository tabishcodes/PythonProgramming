#ANNOTAIONS - as in python we don't need to assign the variable to a specific type
# But with ANNOTATIONS we can do that

def increment(n: int) -> int: # Inside the bracket it assigns the n to int variable & outside after -> this it says that this function returns int value
    return n +1

# To intialize the variable while creating
count : int = 0


#EXCEPTIONS - it helps when we have a error but we need to run the program forward

try:
    result = 2/0
except ZeroDivisionError:
    print("Cannot divide zero!")
finally:
    result = 1

print(result)

#We can also raise a custom exception
#raise Exception("An Error!")

#creating own exception
class DogNotFoundException(Exception):
    pass #this means nothing

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found")

#WITH STATEMENT

filename = 'D:'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
