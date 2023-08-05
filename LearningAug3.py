'''STRINGS - it is inside a "Mark"(Double Quotes) or a 'Kevin'(Single Quotes)
Assign string to a variable'''
name = "Mark"
#String Concatenation
name1 = "Mark" + "Three"
name2 = name + " Three"
name2 += " is an Ironman suit."
print(name2)
print("""Love
You
3000\n""") #Multi Line String

#STRING METHODS
print(name.isupper()) #check if it is uppercase or not
print(name.upper()) #uppercase
print(name.lower()) #lowercase
print(name.islower()) #check if it is lowercase or not
print(name.title()) #First Letter Capital then small
print(name.casefold()) #to lowercase
print(name.capitalize())#First Letter Capital then small
print(name.center(20, "I")) #align to centter syntax- string.center(length, character)
print(name.endswith("k.", 1, 2)) #Check if the string is ending with a dot or not syntax- string.endswith(value, start, end) start & end is int variables.
print(name.endswith("k")) #other usage type
print(name.count("a")) #used to count specific character in a string 
print(name.encode()) #encodes the string default UTF-8, using the specified encoding syntax- string.encode(encoding=encoding, errors=errors)
print("n\ta\tm\te".expandtabs(5)) #it assigns the space to \t and make spaces in between
print(name.find("a")) #find anything in a string syntax- string.find(value, start, end) start & end is int variables
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36)) #format using named indexes
print("My name is {0}, I'm {1}".format("John",36)) #format using numbered indexes
print("My name is {}, I'm {}".format("John",36)) #format using empty placeholders
print(name.index("M")) #occurance of a letter is at position
print(" is tabish".index("a", 1, 7)) #occurance of a letter at specific pointer
print(("," + name).isalnum()) #True if aplhabets & numeric are used else False.
print(name.isalpha()) #True if aplhabets used else False.
print(name.isascii()) #True if b/w a to z else False.