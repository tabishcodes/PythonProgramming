#VARIBLES
name  = "tabish" #String
age = 39         #Int

#EXPRESSIONS 
1+1
"Tabish" 

#STATEMENTS
print(name) 
name1 = "Altu" ; print(name1) #Semicolon(;)can be used to have more then one statement on a sinngle line.

'''Indentation(white space/space) matters in python.
So, if you give space where its not required then
the program while throw the error.'''

#DATA TYPES
name2 = "Shabana" #Anything with quotation mark is a string.
#to know the type of a variable you can do:
print(type(name2))
#you can also test the string by comparing:
print(type(name2) == str)
#we can also us isinstanc like:
print(isinstance(name2, str))

age = 9
print(isinstance(age, int)) #Is an int now
print(isinstance(age, float)) # but not a float
#If I what to convert it to float then
age1 = float(9)
print(isinstance(age1, float)) #now it's a float but not an int.

complex #for complex numbers
bool #for booleans
list #for lists
tuple #for tuples
range #for ranges
dict #for dictionaries
set #for sets


#OPERATORS
name3 = "Bhai" #Assignment Operator

#ARITHMETIC OPERATORS
1+1 #addition operator
2-1 #subtraction operator
2*2 #multiplication operator
4/2 #division operator
4%3 #percent operator - Gives the reminder of the result
4**2 #power operator i.e. 4 with power 2 = 16
ans = 7//3 #floor division operator - does the division and round offs the answer

#We can also use the above operators as:
age2 = 5
age2 += 5 #i.e. age2 = age2 + 5 ; this cn also be used with other operators too

#COMPARISION OPERATORS
a = 1
b = 2

a == b #check if a is equals to b
a != b #check if a is not equals to b
a > b #check if a is greater then b
a < b #check if a less then b
a >= b #check if a is greater than equals to b
a <= b #check if a is less than equals to b

#BOOLEAN OPERATORS
condition1 = True
condition2 = False

not condition1 #is not true (NOT Operator)

condition1 and condition2 #both should be true (AND Operator)
#Something about AND Operator
#Note If the first value is a false, 0 or an empty string then it will display first value.
#IF
print(0 and 1) #this returns 0
print(1 and 0) #this returns 0
print(False and 'hey') #this returns False
print('hi' and 'hey') #this returns 'hey'
print([] and False) #this returns []
print(False and []) #this returns False

condition1 or condition2 #one should be true (OR Operator)
#Something about OR Operator
#IF
print(0 or 1) #this returns 1 as 0 is a false value
print(False or 'hey') #this returns 'hey' as False is a False value
print('hi' or 'hey') #this returns 'hi' as first one 'hi' is not the false value it get displayed
print([] or False) #this returns False as [] this is false value
print(False or []) #this returns [] as False is a False value

'''BITWISE OPERATORS
& perform binary and
| perform binary or
^ perform binary XOR
~ perform binary NOT
<< shift left
>> shift right

is and in Operator
is Identity Operator it is used to compare 2 objects and returns True if both are the same object
in Membership Operator it is used to tell that is value is contain in a list or another sequence

#Ternary Operator - is basically an if-else statement on a single line
For Example
Case 1: Using if-else statement'''
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
#Case 2: Using Ternary Operator

def is_adult1(age):
    return True if age>18 else False
