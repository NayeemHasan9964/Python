# Public and Private Attributes and Methods

class Student:
    def __init__(self,name):
        self.name=name
        
        
class Account:
    def __init__(self,owner,balance=0):
        self.__owner=owner # private Attribute
        self.__balance=balance
        
    def setOwner(self,owner):
        self.__owner=owner
        
    def setBalance(self,balance):
        self.__balance=balance
    
    def printDetails(self):
        print("Owner:",self.__owner)
        print("Balance:",self.__balance)
    
    
        

Acc1=Account("enemy", 2344)
print(Acc1.printDetails())


# Inheritance      