# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:32:02 2019

@author: Muath
"""
#1
class Employee:

    Number : int
    __Name : str
    __Address : str
    __Salary : float
    __Job_title : str
    def __init__(self,number, name, address, salary, job_title):
        self.Number = number
        self.__Name = name
        self.__Address = address
        self.__Salary = salary
        self.__Job_title = job_title

    def getName(self):
        return self.__Name
    
    def getAddress(self):
        return self.__Address
    
    def setAddress(self, NewAddress):
        self.__Address = NewAddress
    
    def getSalary(self):
        return self.__Salary
    def getJob_title(self):
        return self.__Job_title

    def __del__(self):
        print ( self.__Name, 'has been deleted')

#2
Employee1 = Employee(1,"Mohammad Khalid","Amman Jordan",500,"Consultant")
Employee2 = Employee(2,"Hala Rana","Aqaba, Jordan",750,"Manager")

#3
print(Employee1.Number)
print(Employee1.getAddress())
print(Employee1.getName())
print(Employee1.getSalary())
print(Employee1.getJob_title())

print(Employee2.Number)
print(Employee2.getAddress())
print(Employee2.getName())
print(Employee2.getSalary())
print(Employee2.getJob_title())

#4
del Employee1
del Employee2