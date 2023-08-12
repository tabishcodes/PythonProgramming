#Dictionaries
dog = {"name": "Tommy", "age": 8} #syntax- NameOfDict = {"key": "Its value"} it can contain multiple key value pairs

#Changing Dict Values
dog["name"] = "Mike" #how to change the value in a dictionary
dog["age"] = 10 #how to change the value in a dictionary
dog["color"] = 'black'

#Print/Display Method in Dict
print(dog.keys()) #it will display the number of keys in the dict
print(dog.values()) #it will display the number of values in the dict
print(dog["name"]) #you can use double or single quotes inside the square brackets.
print(dog.get("age")) #another method t0 print

#Length Func
print(len(dog))

#in Func 
print("name" in dog) #checking the key in the list

#Copy Func
dogCopy = dog.copy() #this will make a copy of the dict
print(dogCopy)

#Converting Dict keys, values & items to List
print(list(dog.keys())) #it will convert the keys in the dict to list
print(list(dog.values())) #it will convert the values in the dict to list
print(list(dog.items())) #it will convert the items in the dict to list

#Pop/Delete Function
print(dog.pop("name")) #it will delete the item
print(dog.popitem()) #it will pop the last item form the dict
del dog["age"] # it will delete the item


print(dog)