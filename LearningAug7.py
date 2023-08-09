#ENUMS(Enumeration) -readable names that are bounded to constant values or to make a constant.
from enum import Enum

class State(Enum):
    INACTIVE = 0 
    ACTIVE = 1

print(State.ACTIVE) #it doesn't print the calue instead it print the name only
print(State.ACTIVE.value) #now it will display the numeric value
print(State(1)) #it will display State.ACTIVE
print(State['ACTIVE']) #it will display State.ACTIVE
print(list(State)) #this will display the list of values in the enum class State.
print(len(State)) #this will count how many constants or value is inside the class.