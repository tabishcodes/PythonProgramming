num = "1234"
name = "Zeesar"
lin1 = "The banana is yellow."   

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
