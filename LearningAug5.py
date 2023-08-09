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