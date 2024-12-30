from math import factorial
import os
class class1:
    def __init__(self):
        self.a=10
        self.b=20
        self.__c=30

    def add(self):  
        return self.a+self.b
    
    def print_all_variables(self):
        print("var a : ",self.a)
        print("var b : ",self.b)
        print("var c : ",self.__c)
         
    

        




obj=class1()
print(obj.add())
print("var a :",obj.a)
print(factorial(64))

import sys;

var1=sys.argv[1]
var2=sys.argv[2]
os.remove('b1.txt')
print(var1)
print(var2)
print("var c :",obj.__c)


