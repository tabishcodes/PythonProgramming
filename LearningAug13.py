#SETS
#It doen't print the same value 2 times

nameset1 = {"Ram", "Shyam", "Mohan", "Rohan"}
nameset2 = {"Ram"}

#Intersect Function
intersect = nameset1 & nameset2 #interset take outs the common items from the sets
print(intersect)

#Union Function
mod = nameset1 | nameset2 #it will join the sets and print them
print(mod)

#Diiference Funcrion
diff = nameset1 - nameset2 #it will compare the both the sets & display the uncommon values
print(diff)

#Check if the both sets are same or not by following function
check1 = nameset1 < nameset2 #are there same values in nameset2 as in nameset1 ; its false
print(check1)
check1 = nameset1 > nameset2 #are there same values in nameset1 as in nameset2 ; its true
print(check1)

#Length Fuctiom
print(len(nameset1)) #counts number of items in a set

#Convert Set to List
list1 = list(nameset1) #now its converted to list
print(list1) 

#FUNCTIONS - it makes a set of instructor that can we run when needed.
#Initalization of a function starts with def
#It can accept one or many parameters

#Simple Func with no parameter
def Hello():
    print("Hello!")
Hello()

#Func with a parameter and its default value
def Hello(name = "my friend" , age = "Let me guess!"): 
    print("Hello! " + name )
Hello("Rohan")
Hello("Mohan")
Hello()









#VARIABLE SCOPES

#NESTED FUNCTIONS

#CLOSURES

#OBJECTS

#LOOPS

#BREAK CONTINUE
