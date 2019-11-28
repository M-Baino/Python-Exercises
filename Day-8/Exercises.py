# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:44:58 2019

@author: Muath
"""

import numpy as np
import pandas as pd

#1
Array = [2,4,6,8,10]
s = pd.Series(Array)
print(s)

print('_____________________________________')

#2
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
s = pd.Series(d1)
print(s)

print('_____________________________________')

#3
data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)
print( s.describe())

print('_____________________________________')

#4
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],
'd2':[140,0,300,400,200,140,0,700,400,200]
}
Data2 = pd.DataFrame(Data,columns=["d1", "d2"])
Data2.plot()

print('_____________________________________')

#5
dataSample={
         'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
data2 = pd.DataFrame(dataSample)
print (data2)

print('_____________________________________')

#6
dd = {"names" : ['Bob','Jessica','Mary','John','Mel'],"births" : [968, 155, 77, 578, 973]}
dd2 = pd.DataFrame(dd)
dd2.plot.pie(y="births", figsize=(5, 5))

print('_____________________________________')

#7
data = [100, 2200, 300, 400, 500, 600,700,800,900]
d2 = pd.Series(data)
print(d2.describe())
d2.to_csv('myDataFrame.csv', sep='\t')
d2.to_csv('myDataFrame.csv', sep=',')

print('_____________________________________')

#8
dddd = pd.date_range('20000101', periods=4)
df= pd.DataFrame(np.random.randn(4, 2), index=dddd,columns=["A","B"])
print(df)