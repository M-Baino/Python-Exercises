# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:49:08 2019

@author: Muath
"""

class person:
    def hello(self): # == self.. (current object)
        print('Hi')
p = person()
p.hello()

print("_____________________________________________")

# Constructor or initializer:  def __init__(self, name): 
# Destructor:  def __del__( self ):

class Person:
# constructor or initializer => b3ml initialization lal object
    def __init__(self, name):
        self.name = name
# method which returns a string
    def whoami(self):
        return "I am " + self.name
# destructors
    def __del__(self):
        print ( 'I have been deleted')

p1 = Person('tom')
print(p1.whoami())
print(p1.name)
del p1

##### training on constructor & destructor
class Person2:
    def __init__(self,name):
        self.name = name
    def who(self):
        return "I'm " + self.name
    def __del__(self):
        print('I have been deleted')
p = Person2('Bagara')
print(p.who())
print(p.name)
del p

"""
Apublic // methods, properties or attributes
_Bprotected // methods, properties or attributes
__private  // methods, properties or attributes
"""

class Encapsulation(object):
    def __init__(self,a,b,c):
        self.Apublic = a
        self._Bprotected = b
        self.__Cprivate = c
    def getprivate(self):
        return self.__Cprivate
    def setprivate(self, s):
        self.__Cprivate = s
x = Encapsulation(11,7,13)
print(x.Apublic)
print(x._Bprotected)
#print(x.__Cprivate) error
x.setprivate(15)
print(x.getprivate())

print("_____________________________________________")

class Parent(object):
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary

    def public(self):
        print('calling public')
    def _protected(self):
        print('calling protected')
    def __private(self):
        print('calling private')

###### complete from python slides


class A(object):
    def __init__(self):
            print("world")
class B(A):
    def __init__(self):
            print("hello")
b1=B()

print("_____________________________________________")

class A(object):
    def __init__(self):
        print("world")
class B(A):
    def __init__(self):
            print("hello")
            super().__init__()
            A.__init__(self)
b1=B()

print("_____________________________________________")

class A():
    def __init__(self):
        self.__x = 1
    def m1(self):
        print("m1 from A")
class B(A):
    def __init__(self):
        self.__y = 1
    def m1(self):
        print("m1 from B")
c = B()
c.m1()

print("_____________________________________________")

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )

c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2
print(c3.getRadius())

print("_____________________________________________")

