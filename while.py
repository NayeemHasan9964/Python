print("Learning While Loop")
# Question 1: Print numbers from 1-100
# i=1
# print(type(i))
# while i<=100:
#     print(i)
#     i+=1

# Question 2:Print numbers from 100-1    
# j=100    
# while j>=1:
#     print(j)   
#     j-=1 
    
# Question 3:Print the multiplication of given number

# n = int(input("Enter the number : "))
# print("Given number is",n)
# i=1
# while i<=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1
    
# Question 4: Print the sqaures of number
i=1
list_Squares=[]
while i<=10:
    list_Squares.append(i*i)
    i+=1
print(list_Squares) 
    
# Question 5: Find the number x in tuple

x=int(input("Enther the Number :"))    
tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)   
idx=0
while idx<len(tuple):
     if tuple[idx]==x:
         print("Number Found")
     else:
        print("Not Found")  
     idx+=1      
    