# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:19:27 2019

@author: Muath
"""

#1
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

if num1 > num2:
    print(num1, "is the greatest")
else:
    print(" ", num2, "is the greatest")

#2
number = int(input("Enter a number.."))
i=1
while i <= 10:
    print(number, "X", i, " = ", number * i)
    i+=1

#3
    """
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end = ' ')
        j += 1
    print()
    i += 1
    """
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end = ' ')
        j += 1
    print()
    if i == 5:
        k = 4
        while k >=1:
            l = 4
            while l >= k:
                print('*', end = ' ')
                l -= 1   
            k -= 1
            print()
    i += 1



#4
# The output is: ["x","y","z","b","c"]

#5
# The output is: 12,15,18,21,24 each in a separate line

#6
# The output is: 1,2,3 each in a separate line

#7
m = int(input("Enter a number"))
i = 0
total = 0
while i <= m:
    total += i
    
    i += 1
print(total)

#8
number = int(input("Enter a number"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
 
#9
###### square of stars #######

#10
while True:
    try:
        number = input("Enter an integer number")
        number = int(number)
        break
    except ValueError:
        print("Invalid input.. please try again")
print("Mission successful =)")

#11
# The output is: Error Occurred and Handled
            