# Most occuring Characters in a String
# def most_common_character(s):
#     x = list(s)
#     print(x)
#     for i in x:
#         if i != "h":
#             return i
#         elif s[0]=="h":
#             return "l"
# print(most_common_character("hello world"))          
        
# Sum of Digits
# def sum_of_digits(n):
#     sum = 0
#     while n > 0:    
#         sum += n % 10
#         n //= 10
#     return sum
# print(sum_of_digits(12345))  

# function to save time
# def time_saved(distance, speed1, speed2):
#     print(distance/speed1- distance/speed2)
#     return round(distance/speed1- distance/speed2,2)
# print(time_saved(200,60,80)) 

# Find the index of the first vowel in the String
# def first_vowel_index(s):
#     x = s.lower()
#     z = list(x)
#     y = ['a','e','i','o','u']
#     for i in range(0 ,len(x)):
#         for j in range(0 , len(y)):
#             if x[i] == y[j]:
#                 return i
# print(first_vowel_index('PYTHON'))

# Function to check given number is a Sastry number or not
# import math

# def is_sastry(n):
#     # Concatenate n and n+1
#     concatenated_number = int(str(n) + str(n + 1))
    
#     # Check if concatenated_number is a perfect square
#     sqrt = int(math.sqrt(concatenated_number))
#     print(sqrt)
    
#     return sqrt * sqrt == concatenated_number  
# print(is_sastry(183))    

# Function to Remove special characters from a String
# def remove_special_chars(s):
#     special_char_list = {'@', '#', '!', "*", '.', '$', '%', '^', '<', '>', '&','(', ')', '_', '+', '-', '=', '~', ',', '?', '/'}
#     for char1 in s:
#         if char1 in special_char_list:
#             s = s.replace(char1, '')
#     return s
# print(remove_special_chars("hello@ world!!*")) 

# Function to calculate the hypotenuse of the right angle traingle
import math
def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
    
print(calculate_hypotenuse(3,4))



  