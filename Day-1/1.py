# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
str = "So Muath wu"
print(str)

# Hacking! HAHAHA

ddr = 1
print(ddr)
print('Space', 'Between', sep = ' ') # sep => separate
print('A', 'B', end = ' ')
print('same line')
print('Devi', 'ded', sep = '\n')
print('%5d' %(6)) # printing after 5 spaces.. d => decimal
print('%05d' %(6)) # 0's instead of spaces

age = input("What is your Age? ")
print(age)
print ( type(age)) # age type is string (default)

age = int(input("What is your Age? "))
print(age)
print ( type(age)) # age type is now integer

cities_canada = eval(input("Largest cities in Canada: "))
print(cities_canada)
print(type(cities_canada)) # (eval) evaluates the variable => it will guess the type of the variable excluding "string"

"""
(casting) is: changing the types of variables

-Examples:
    
int(12.1) => 12
float(20) => 20.0
str(10) => ’10’
int(‘100’) => 100
"""

x, y, z = "Orange", "Banana", "Cherry" # defining multiple variables 
print(x,y,z) 

n = 11 // 3
print(n) # result will be integer (3)

reminder = 11 % 3
print(reminder) # => mod in VB

# help(print)   or   print?   to get help from python itself



