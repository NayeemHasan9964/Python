# Public and Private Attributes and Methods

# class Student:
#     def __init__(self,name):
#         self.name=name
        
        
# class Account:
#     def __init__(self,owner,balance=0):
#         self.__owner=owner # private Attribute
#         self.__balance=balance
        
#     def setOwner(self,owner):
#         self.__owner=owner
        
#     def setBalance(self,balance):
#         self.__balance=balance
    
#     def printDetails(self):
#         print("Owner:",self.__owner)
#         print("Balance:",self.__balance)
    
    
        

# Acc1=Account("enemy", 2344)
# print(Acc1.printDetails())


# Inheritance

class prototype():
    @staticmethod
    def power1():
        print("ShapeShift")
    
    @staticmethod
    def  power2():
        print("Consume")   
        
    @staticmethod
    def  power3():
        print("Claws")
    
    @staticmethod
    def  power4():
        print("Whiplash")
        
        
class part1(prototype):
    def __init__(self,name):
        self.name = name
        print("Character Name is: ", self.name)
            
class part2(part1):
    def inheritedPowers(self):
        print("Inherited Powers from AlexMercer And my name is " , self.name)
    

prototype1 = part1("AlexMercer")
prototype1.power1()
prototype1.power2()
prototype1.power3()
prototype1.power4()

prototype2 = part2("JamesHeller")
prototype2.inheritedPowers()
prototype2.power1
prototype2.power2()
prototype2.power3()
prototype2.power4()


