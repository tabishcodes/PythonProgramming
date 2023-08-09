num = "1234"
name = "Zeesar"
lin1 = "The banana is yellow."

#USER INPUTS
#name = input("What is your name ? ")
print("Your Name is " + name)

#CONTROL STATEMENTS

#IF STATEMENT
condition = True

if condition == True:
    print("The condition was true")
else:
    print("The condition was false")
print("outside if statement")
 
#LISTS - its is used to group multiple values of multiple types
studentName = ["Alfiya", 1 , "Noman", True] #list of values

#Checking the value in List
print("Noman" in studentName) #in is used the check the value is in the list or not
print(studentName[1]) #used to display the values in the list with there indexes

#Changing value with index use
studentName[2] = "Rashid" # change list values with the use of index value
print(studentName) #prints the whole list

#Different Printing Methods
print(studentName[-1]) #if we count the list in the reverse direction then the first value index is -1.
print(studentName[1:3]) #doing part of the list - index value 1 to 2 will be displayed but index value 3 will not be displayed
print(studentName[1:]) #now it will display from index value 1 to the end of the list
print(studentName[:3]) #now it will display from starting to the index value 3
print(len(studentName)) #used to find the length/values in the list

#Remove Function
studentName.append("Faruk") # used to add a single value in the list
print(studentName) #prints the whole list with added append value

#Extend Function
studentName.extend(["Faruk", 2, False]) # used to add multiple values or another list into the list; and use the curve n square brackets
print(studentName) #prints the whole list with added extended values
studentName += [1, "Amir", False] # += is used as an extended funtion and use only square brackets
print(studentName) #prints the whole list with added extended values

#Remove Function
studentName.remove("Alfiya") #it will remove the following item from the list
print(studentName) #prints the whole list

#Pop Function
studentName.pop() #it will pop/remove the last/default item from the list
print(studentName) #prints the whole list

#Insert Function - Inserts an item in between the list
studentName.insert(2, "Test") 
print(studentName) #prints the whole list 

#For adding multiple items in between the list we need slices
studentName[1:2] = ["Test1", "Test2", "Test3"]
print(studentName) #prints the whole list 

#List Sorting
