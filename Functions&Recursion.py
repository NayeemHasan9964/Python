# Functions
#Function Defination
# def add(a, b): #Function parameters
#     return a + b

# def subtract(a, b):
#     return a - b

# Sum=add(2,4) #Function Arguments
# Sub=subtract(5,5)

# print(Sum,Sub)

# WAF to print the len of the list(List is the parameter)
# def printList(prac):
 #  return len(prac)

# Length=printList([1,2,3,4])
# print(Length)

#WAF to print elements in a list in single line(List is the parameter)
# def printElements(elements):
#     for i in elements:
#         print(i, end=" ")
# printElements([1,3,4,5,6])


# WAF to print the factorial of n(n is the parameter)
def factorial_Of_n(n):
    fact=1
    if n==0:
        print("Cannot start with Zero")
    for i in range(1,n+1):
        fact*=i
    return fact
    
print(factorial_Of_n(5))
      