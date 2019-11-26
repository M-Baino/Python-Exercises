# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:26:41 2019

@author: Muath
"""
#1
Spacing = '   '
print('Hello', Spacing + 'Hello', Spacing + Spacing+'Hello', sep = '\n')

#2
print('Orange Academy \n'*20)

#3
# the output is: 1.0102.8103.0104.2

#4
first_num = int(input("Enter a number.."))
second_num = int(input("Enter another number.."))
print((first_num))
print((second_num))

#5
n1, n2, n3, n4, n5 = int(input("Enter five numbers (1st Num)")), int(input("Enter 2nd num")),int(input("3rd num")),int(input("4th num")),int(input("5th num")) 

result = n1 + n2 + n3 + n4 + n5
print(result / 5)
#6
"""
The output is:
    
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
"""

#7
# x1 is not defined

#8
"""
5x=10 "cannot declare a variable which begins with a number"
x_q$ ="Orange" "($) char. is not allowed in python for variable declaration"
A B = 14 "vaiable name cannot contain spaces"
 """  
#9 & #10 are identical to #7 #8
 
#11
#The output is: Cheers, Mate!
 
#EX12
Name = input("Enter your name")
Age = int(input("Enter your Age"))
print ("Dear", Name ,  ", The year you will turn 100 is" , int(2019 - Age + 100))

#13

base = int(input("Enter the base of a triangle"))
hight = int(input("Enter the hight of that triangle"))
print("Triangle's area =", (base*hight)/2)

#14
"""
The output is:
    
14
8
33
3.6666666666666665
3
2
11
11
11.0
(3, 2)
1331
1331
True
False
True
"""