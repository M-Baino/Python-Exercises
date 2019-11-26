# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:39:08 2019

@author: Muath
"""

a, b = 1, 10
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")
    
a, b = 1, 10
max = a if (a > b) else b
print(max)

if 'a' in ['b','c','a']:
    print("a is in the list")
else: print("a is not in the list")

a=10
b=5
if a > b: print("a is greater than b")

a = 2
b = 330
print("a") if a > b else print("b")

a = 1000
b = 330
print("a") if a > b else print("=") if a == b else print("b")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
    
    ############# Practice ###############
    
a = input("Enter 1st num")
b = input("Enter 2nd num")
if (a < b):
    print(a,b)
else:
    print(b, a)
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    print("Under Age")
    average = float(input("Enter your school average please"))
    if average >= 90:
        print("Excellent Average")
    elif average >= 50:
        print("Passed")
    else:
        print("Failed")
else:
    job = input("Enter your job title please")
    print("\n", name, age, job)

    ############# The End ###############

    ### Loops ###

for a in range(3): # from 0 to 2
    print(a)

print("___________________________________________ \n")

for a in range(1,5,2): # from 1 to 5 .. 2 steps       "5 OUT OF RANGE"
    print(a)

print("___________________________________________ \n")

for item in ['Jordan','US','UK']:
    print(item)

print("___________________________________________ \n")

for x in "name":
    print(x)

print("___________________________________________ \n")

fruits = ["apple", "banana", "cherry"] # OUTPUT: apple
for x in fruits:
    print(x)
    if x == "banana":
        break

print("___________________________________________ \n")

fruits = ["apple", "banana", "cherry"] # OUTPUT: apple & cherry
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("___________________________________________ \n")

for x in range(6):
    print(x)
else:
    print("Finally finished!") # this -else- is not recomended

print("___________________________________________ \n")

color = ["red", "green", "blue"]
fruits = ["apple", "banana", "cherry"]
    ## nested loop: ##
for x in color :
    for y in fruits:
        print(x, y)

print("___________________________________________ \n")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w)) # len() = length

print("___________________________________________ \n")

l = ["eat","sleep","repeat"]
for count,e in enumerate(l): # enumeration
    print (count,e)

print("___________________________________________ \n")

i=0
while i<4:
    print(i)
    i+=1

print("___________________________________________ \n")

while True:
    a=input('>')
    if a=='exit':
        break
    print (a)

print("___________________________________________ \n")

colors = ["red", "green", "blue", "purple"]
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

print("___________________________________________ \n")

    ############# Loops Practice ###############

i = 1
star = '*'
while i <= 10:
    print(star)
    i += 1

print("___________________________________________ \n")

i = 1
star = '*'
while i <= 20:
    print( star, end = " ")
    i += 1
print('\n')

print("___________________________________________ \n")

i = 0
j = 0
star = '*'
while i <= 8:
    j=0
    while j <= i:
        print(star,end="")
        j += 1
    print()
    i += 1
    
print("___________________________________________ \n")

# reversed triangle #

print("___________________________________________ \n")

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")

print("___________________________________________ \n")

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")
    
### something like hacking:
    
star = "*"
space = "          "
for test in range(10):
   print(star)
   star += "*"
num = len(star)-1

for two in range(10):
   print(star[slice(num)])
   num-=1
num = len(space) - 1
