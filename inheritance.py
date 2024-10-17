class Hello:
    name = "Sonu"
    num =1000
    def __init__(self,a,b):
        self.a= a
        self.b= b

    def calling_name(self):
        print("Hello" +" "+ self.name)

    def sum_of_two_numbers(self):
        return self.a + self.b + Hello.num
obj = Hello(4,2)
var = obj.name
print(var)
obj.calling_name()
summation = obj.sum_of_two_numbers()
print(summation)