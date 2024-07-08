# Public and Private Attributes and Methods

class Student:
    def __init__(self,name):
        self.name=name
        
        
class Account:
    def __init__(self,owner,balance=0):
        self.__owner=owner # private Attribute
        

Acc1=Account("hulk", 0)
print(Acc1.__owner)        