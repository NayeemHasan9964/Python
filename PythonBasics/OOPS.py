# Classes are blueprints of Objects
# Objects are instances of classes
# Classes are defined using the class keyword
# Class names should be in CamelCase
# Class names should be nouns, in singular form
# Class names should be descriptive of the object they represent
# Class names should be unique within a module
# Class names should be short, but not too short
# Class names should be meaningful
# Class names should be consistent with the naming convention of the language

class Student(): # Syntax of Class
    name="Karan" # Attributes of Class
    
s1=Student() # Object Creation
print(s1.name) # Accessinmg Attributes of Class

# Constructor is a special method of a class
# Constructor is invoked automatically when an object is created

class Car():
    # Parameterized Construtor
    def __init__(self,make,model,year): # Constructor
        self.make=make # Attributes of Class
        self.model=model # Attributes of Class
        self.year=year # Attributes of Class
        
    def print_details(self): # Method of Class
            print("Make:",self.make)
            print("Model:",self.model)
            print("Year:",self.year)
            
c1=Car("Mercedes","ZLS",2022)
c1.print_details()

# WAP to create class that takes name and marks of 3 Subjects as Arguments in Constructor
# and display Avg of marks using method

class Student():
    def __init__(self,Fullname,marks):
        self.name=Fullname
        self.marks=marks
        
    def averageOfMarks(self):
        sum=0
        for val in self.marks:
            sum=sum+val
            avg=sum/len(self.marks)
        print("Hi", self.name, ",Your Average is:" , avg)
    
s1=Student("AlexMErcer",[23,65,68])

s1.averageOfMarks()

# Creata class to get bank account details(Optional)
