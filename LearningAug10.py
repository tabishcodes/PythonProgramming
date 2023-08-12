studentName = ["Alfiya", "Noman", "aman", "Juned"]
studentRollNo = [1, 5, 6, 2]

#List Sorting
#Sorting modifies the orignal list content of the list so we can copy a list
studentNameCopy = studentName[:]
studentRollNoCopy = studentRollNo[:]

studentName.sort() #for using sort the list should have a single variable type also the upper case letter come first and then comes the lower case letter.
print(studentName)

#to deal with the lower case letter we can add
studentName.sort(key=str.lower) #it will sort both upper & Lower case alphabetically
print(studentName)

studentRollNo.sort()
print(studentRollNo)

print(studentName)
print(studentRollNo)
print(studentNameCopy)
print(studentRollNoCopy)

studentName = ["Alfiya", "Noman", "aman", "Juned"]
studentRollNo = [1, 5, 6, 2]
#There is the second way to sort without making a copy of a list i.e.
print(sorted(studentName, key=str.lower)) #using this way you don't need a copy of a list
print(studentName)

#Tuples
#Fundamental python data structure they allows to make immutable groups of objects
#Tuples can't be modified once it is created
names = ("Alfiya", "Noman", "aman", "Juned")

print(names[1]) #You can get the values of the tuples by reffering the indexs
print(names.index("Noman")) #You can also get the index of the following value

print(len(names)) #print number of items in the tuples

print("Noman" in names) # checks if the item is present in the tuples or not

print(names[1:3]) #parting the tuples using slices

#Tuple Sorting
print(sorted(names, key=str.lower)) #as it sorts the tuple but the items in the original tuples will remain same as original

newnames = names + ("Haris", "Elena") #If we want to add new items in a tuple then we have to make a new tuple because wwe can't modify the orignal one
print(newnames)