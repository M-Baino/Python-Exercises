# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:34:21 2019

@author: Muath
"""
import numpy as np
import matplotlib.pyplot as plt

# 1
print('________________________________')
zeros = np.zeros(10, np.int)
print(zeros)

ones = np.ones(10, np.int)
print(ones)

fives = np.ones(10, np.int) * 5
print(fives)

# 2
print('________________________________')
ar = np.arange(30, 71)
print(two)

# 3
print('________________________________')
arr = np.arange(30, 71, 2)
print(three)

# 4
print('________________________________')
abb = np.arange(9).reshape(3, 3)
print(four)

# 5
print('________________________________')
rand_num = np.random.normal(0, 1, 1)
print(rand_num[0])

# 6
print('________________________________')
aa = np.arange(12).reshape(3, 4)
print(aa)

# 7
print('________________________________')
ab = np.arange(20)
ab[(ab > 8) & (ab < 16)] *= -1
print(ab)

# 8
print('________________________________')

a = np.array([1, 8, 3, 5])
b = np.random.randint(0, 11, 4)
c = a * b
print(c)

# 9
print('________________________________')
n = np.arange(6).reshape(2, 3)
print('nine:\n', n)
print('"nine" array rows: ', n.shape[0])
print('"nine" array columns: ', n.shape[1])

# 10
print('________________________________')
abc = np.arange(27).reshape(3, 3, 3)
print(abc)

# 11
print('________________________________')
a = np.array([9, -1, 2, 3])
b = np.array([1, -6, 0, 10])
c = np.array([[1, 8, 2, 5], [3, 1, 7, 9]])

print('a - b:', a - b)
print('a * b:', a * b)
print('a,dot(b):', a.dot(b))
print('a * 2:', a * 2)
print('np.sin(a):', np.sin(a))
print('a < 3:', a < 3)
print('a.sum(): ', a.sum())
print('a.sum(axis=0):', a.sum(axis=0))
print('c.sum():', c.sum())
print('c.sum(axis=0)', c.sum(axis=0))
print('a.min():', a.min())
print('a.mean():', a.mean())
print('a average(): ', np.average(a))
print('a median():', np.median(a))
print('a std(): ', np.std(a))
print('a var():', np.var(a))
print('c.cumsum():', c.cumsum())
print("a[1:2] : ", a[1:2])
print("a[2:] : ", a[2:])
print("c[-1] : ", c[-1])

# 12
print('________________________________')
x = np.arange(1, 50)
y = [value * 3 for value in x]
plt.plot(x, y)
plt.title('Draw a line .')
plt.ylabel('Y-axis')
plt.xlabel('X-axi')
plt.show()

# 13
print('________________________________')
xa = [10, 20, 30]
xb = [10, 20, 30]
plt.figure()
plt.plot(xa, [20, 40, 10], label="line1")
plt.plot(xb, [40, 10, 30], label="line2")
plt.title("Tow or more lines on same plot with suitable legends")
plt.legend(loc='upper right')
plt.show()

# 14
print('________________________________')
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

# 15
print('________________________________')

objects = ('Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++')
y_pos = np.arange(len(objects))
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(y_pos, popularity, align='center', color=[
        'red', 'black', 'green', 'blue', 'yellow', 'blue'])
plt.xticks(y_pos, objects)
plt.ylabel('Popularity')
plt.title('Languages')
plt.show()