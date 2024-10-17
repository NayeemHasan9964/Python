from inheritance import Hello

class ChildImplementation(Hello):
    num2 = 500
    def __init__(self):
        Hello.__init__(self,2,10)

    def total_summation(self):
        return self.num2 + self.num + self.sum_of_two_numbers()
obj = ChildImplementation()
print(obj.total_summation())


