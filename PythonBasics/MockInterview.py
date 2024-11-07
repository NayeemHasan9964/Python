# def Reverse_String(String):
#     lower_case = String.lower()
#     reversed_string = lower_case[::-1]
#     return reversed_string
# print(Reverse_String("MADAM123"))

# Write today is sunday
# def reverse_words(String):
#     return " ".join(String.split()[::-1])
#
# print(reverse_words("today is sunday"))

# # Function to check if a number is prime
# # Python program to display all the prime numbers within an interval
# lower = 2
# upper = 100
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#
# list1 = [99,88,77,66,55,44,33,22,11]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j] = list1[j],list1[i]
# print(list1)

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str  # Prepend each character to the result
#     return reversed_str
#
# # Test
# input_str = "Hello"
# print(reverse_string(input_str))  # Output: "olleH"

# def sum_of_squares(numbers):
#     sum = 0
#     for i in range(len(numbers)):
#         sum = sum + numbers[i]**2
#     return sum
# print(sum_of_squares([1,2,4]))

# target = 9
# def target_sum(lst):
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i]+lst[j]==target:
#                 return i,j
# print("The Indices which gives target sum are",target_sum([1,2,4,7]))


# def find_maxNum(lst):
#     max_of_list = lst[0]
#     for i in range(len(lst)):
#         if lst[i]<max_of_list:
#             max_of_list  = lst[i]
#     return max_of_list
# print(find_maxNum([55,66,99,88,77,44]))

#0,1,1,2,3,5...
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1
#
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2


