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