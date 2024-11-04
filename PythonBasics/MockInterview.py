# def Reverse_String(String):
#     lower_case = String.lower()
#     reversed_string = lower_case[::-1]
#     return reversed_string
# print(Reverse_String("MADAM123"))
#
# # Write today is sunday
# def reverse_words(String):
#     return " ".join(String.split()[::-1])
#
# print(reverse_words("today is sunday"))


# Function to check if a number is prime
# Python program to display all the prime numbers within an interval

# lower = 2
# upper = 100
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

list1 = [99,88,77,66,55,44,33,22,11]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
