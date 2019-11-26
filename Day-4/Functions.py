# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:32:40 2019

@author: Muath
"""

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry", "strawberry", "pumpkin"]
my_function(fruits)

print ("_________________________________________________")

def second_ftn(x):
    return 5 * x
print (second_ftn(5))
print (second_ftn(6))
print (second_ftn(7))

print ("_________________________________________________")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Sam", child2 ="Tobias", child3 = "Khalid")

print ("_________________________________________________")

def adder(*num):
    sum = 0

    for n in num:
        sum += n
        print("sum: ", sum)
    
adder(15,14,60,17)

print ("_________________________________________________")
"""
def ftn(arg1, *argv): #if we flip the arguments we will get an error!
    print("First argument: ", arg1)
    for arg in argv # we are still getting an error.. xD
        print("Next argument from *argv: ", argv)

ftn('h','w','z')

print ("_________________________________________________")

def some_args(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
my_list = [2,3]
some_args = (1, my_list)
"""
print ("_________________________________________________")

def ftn2 (**many_args):
    for key,value in many_args.items():
        print("%s == %s" %(key,value))

ftn2(first = 'geeks', mid = 'for', last = 'geeks')

print ("_________________________________________________")

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

print ("_________________________________________________")

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

print ("_________________________________________________")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

print ("_________________________________________________")

sum = lambda x, y : x + y
print ( sum(56,7))

print ("_________________________________________________")

x= (lambda x, y: x + y)(2, 3)
print(x)

print ("_________________________________________________")

print((lambda x, y: x + y)(2, 3))

print ("_________________________________________________")

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

print ("_________________________________________________")

list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])) 

print ("_________________________________________________")

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)

print ("_________________________________________________")

MyList = [0,1,2,3,4,10,13,22,25,100,120]
print("squared List:", list(map(lambda x: x**2, MyList)) )

print ("_________________________________________________")

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241,
9.01344, 32.00013]
result = list(map(round, circle_areas, range(1,7)))
print(result)

print ("_________________________________________________")

MyList = [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers = list(filter(lambda x: x % 2, MyList))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, MyList))
print(even_numbers)

print ("_________________________________________________")

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)

print ("_________________________________________________")
#without zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)

print ("_________________________________________________")
#with zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(zip(my_strings, my_numbers))
print(results)

print ("_________________________________________________")

from functools import reduce
x= reduce(lambda a,b: a+b,[23,21,45,98])
print(x)

print ("_________________________________________________")

import functools
# initializing list
lis = [ 1 , 3, 5, 6, 2, ]
# using reduce to compute sum of list
print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))
# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 

