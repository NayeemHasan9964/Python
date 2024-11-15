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

# WAF to print elements in a list in single line(List is the parameter)
# def printElements(elements):
#     for i in elements:
#         print(i, end=" ")
# printElements([1,3,4,5,6])


# WAF to print the factorial of n(n is the parameter)
# def factorial_Of_n(n):
#     fact=1
#     if n==0:
#         print("Cannot start with Zero")
#     for i in range(1,n+1):
#         fact*=i
#     return fact
    
# print(factorial_Of_n(5))



# Recursion-->When a function calls its self again is called "Recursion"
# Its similar to For and while loops

# def RecursionExample(n):
#     if (n==0): # Base case
#         return 
#     print(n)
#     RecursionExample(n-1)
# RecursionExample(5)

# # WAP recurison program to calculate sum of N natural numbers

# def cal_n_Natural_Numbers(n):
#     if n==0:
#         return 0
#     else:
#         return n+cal_n_Natural_Numbers(n-1)

# print(cal_n_Natural_Numbers(10))    

# WAP using recursion to print elements in the list

#  def printElements(list,idx):
#    if idx==len(list):
#       return
#    print(list[idx])
#    printElements(list,idx+1)
    
#  printElements([1,2,3,4,5],0)
    
 
#Write a function to split the restaurant bill among friends.
# Take the subtotal of the bill and the number of friends as inputs.
# Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
# Return the amount each friend has to pay, rounded off to two decimal places.    




      