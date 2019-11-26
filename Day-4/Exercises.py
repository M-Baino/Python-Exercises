# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:26:20 2019

@author: Muath
"""

#1 The output is: 6,15,33

#2
from functools import reduce
multi = reduce(lambda a,b: a*b , [1,2,3,4,5,6,7,8])
print(multi)

#3
mul = lambda x, y : x * y
print ( mul(5,10) )

#4
num_list = filter(lambda range(-5,5): return num if num < 0 )

#5

