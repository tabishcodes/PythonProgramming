num = "1234"
name = "Zeesar"
lin1 = "The banana is yellow."

#STRING METHODS
print(num.isdecimal()) #returns true if the all the characters are decimal (0-9) else false.
print("\u0030".isdecimal()) #returns true if the value of the unicode is a number.
print(num.isdigit()) #same as isdecimal but exponents like ² (power value), are also considered to be a digit.
print("q adc".isidentifier()) #returns true is a string contains alphanumeric letters (a-z) and (0-9), or underscores (_) but it cannot start with a number, or contain any spaces in start or inbetween.
print(num.isdecimal()) #returns true if the string contains all numeric values (0-9) with no decimal point, negative value, power value or rational value.
print(num.isprintable()) #returns true if the values are printable else false
print(num.isspace()) #returns true if all the charcters in the string is whitespaces
print("#$".join(num)) #return the string with joined iterable in between. Syntax- string.join(iterable)
x = name.ljust(20) ; print(x, "is a name") #returns the left aligned string with specific spacing value in the brackets.
x = name.ljust(20, "I") ; print(x, "is a name") #spacing is filed by the specific character in the double quotes
x = name.rjust(20) ; print(x, "is a name") #returns the right aligned string with specific spacing value in the brackets.
x = name.rjust(20, "I") ; print(x, "is a name") #spacing is filed by the specific character in the double quotes
x = "     Shawn      ".strip() ; print("The", x, "ate everything.") #return the value of string by removing  space of it.
x = "...,,,Shawn.......".strip(",.,....") ; print("The", x, "ate everything.") #also remove the specific chars
x = "     Shawn      ".lstrip() ; print("The", x, "ate everything.") #return the value of string by removing left space of it.
x = "...,,,Shawn.......".lstrip(",.,....") ; print("The", x, "ate everything.") #also remove the specific left chars not right if needed
name1= "John Murphy" ; x= str.maketrans("J", "I") ; print(name1.translate(x)) #it returns the mapping table that can we used with translate  to replace specific character.
name1= "John Murphy" ; x= str.maketrans("J", "I", "h") ; print(name1.translate(x)) #maketrans(x, y, z) - the first x value in the bracket is what char we choose, y second is by which it is replace & z third is which value is to be deleted.
print(lin1.partition("banana")) #it returns the a tuple with 3 elements by seperating the following char from it.
print(lin1.partition("apple")) #it will return the whole string in 1st tuple if the char is not found in the string; the 2nd & 3rd tuples will be then empty.
print("The banana & banana is red & yellow.".replace("banana", "apple", 1)) #the value in the last decides how many times value will be changes
print(lin1.rfind("banana")) #finds the value and returns the pointer place else return -1
print(lin1.rfind("banana", 6, 10)) #finds the value b/w specific range and returns the pointer place else return -1
print(lin1.rindex("banana")) #finds the value and returns the pointer place else return error
print(lin1.rindex("banana", 0, 10)) #finds the value b/w specific range and returns the pointer place else return error
print(lin1.split()) #will split the string where there is space in b/w i.e. after every word
print(lin1.split("a", 1)) #split the string by replacincing the specific char and only for give times
print("The banana \n is yellow.".splitlines()) #splits a string into a list ; splitting is done at line breaks
print(lin1.startswith("The")) #if it starts with the value in the startswith bracket value then its true else false
print(lin1.startswith("The", 6, 10)) #check the char between specific positions
print(lin1.swapcase()) #return opposite cases of every char in the string
mydict = {83:   80} ; txt2="Steel" ; print(txt2.translate(mydict))
print("110".zfill(10)) #fill the starting pointers with 0 then at last display the value.

#ESCAPING CHARACTERS
print("Bra\"ein") # \ (backslash) will make the next char does'nt effect the coming char.
print("Bra\nein") # \n means new line
print("Bra\\ein") #this is used to use a \ in between

#STRING CHARACTERS & SLICING
print(name[0]) #this will display the index value as followed.
print(name[1:5]) #this will display the index value between the following value.

#BOOLEANS
done = True #in numerics +ve & -ve values ; in string any char in double quotes are considered true but 0;empty str is considered as false. 

if done:
    print("Yes")
else:
    print("No")\
    
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) #as it says any if anyone is true then rest is also true.

print(read_any_book)

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])

print(ready_to_serve) #as it says all means if all the values are true then its true else false

#NUMBER DATA TYPES
num1 = 2+3j
num2 = complex(2,3)

print(num2.real,num2.imag)

#BUILT-IN-FUNCTION
print(abs(-5.5)) #it make every value +ve
print(round(5.49)) #it round-off (if its below 0.50 then it's 0 & if it's equal to or more then 0.50 the its 1)
print(round(5.49, 1)) #now in the second parameter we can set at what decimal point we need to round off.

#ENUMS(Enumeration) -readable names that are bounded to constant values.
from enum import Enum

class State(Enum):
    INACTIVE = 0 
    ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])