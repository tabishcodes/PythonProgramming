#ARGUMENTS OF COMMAND LINE
#running a program with Terminal Code
#Syntax: python FileName.py

import sys #always import anything at the top of the file

"""
print(sys.argv)

name = sys.argv[1]
print("Hello " + name )


import argparse #helps to comunicate information back to the user

parser = argparse.ArgumentParser(
    description="Is is argparse"
)

parser.add_argument('-c', '--color', metavar= 'color', required= True, choices={'red', 'yellow'}, help= 'the color to search for')

args = parser.parse_args()

print(args.color)
"""
#LAMBDA FUNCTIONS 
#they are tiny functions and online have one expression with no name
# the body must be a single expression
#to print lamba value you to assign it to the varible
#An expression returns the value but statement does not

lambda num : num * 2

SumOfTTwo = lambda num : num + 2

print(SumOfTTwo(10)) #this is how values are passed in the lambda function

#MAP, FILTER & REDUCE this all are a funvtion

#Map - it is used to run a function upon each item like a list
numbers = [1,2,3]

def double(a):
    return a * 2
result = map(double, numbers)

print(list(result)) #runs the fuction on each items of the list

#we can also do using the lambda function
numbers = [1,2,3]

double = lambda a : a*2
result = map(double, numbers)

print(list(result))

#Filter  
numbers = [1,2,3]

def isEven(n):
    return n % 2 == 0
 
result = filter(isEven, numbers)

print(list(result))

#we can also do using the lambda function
numbers = [1,2,3]

result = filter(lambda a : a%2 == 0, numbers)

print(list(result))

#Reduce - it is used to calculate the value out of a sequence
from functools import reduce

expenses = [ #this is the list which is stored  as tuples
    ('Dinner', 80),
    ('Car Repair', 120) 
]

sum = reduce(lambda a,b: a[1] + b[1], expenses)

print(sum)