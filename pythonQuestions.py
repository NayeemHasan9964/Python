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
# import math
# def calculate_hypotenuse(a, b):
#     return math.sqrt(a**2 + b**2)
    
# print(calculate_hypotenuse(3,4))

# Function to create Dictionary from a List where Keys are the values of list and values are 
# Squares of the list

# def numbers_to_dict(numbers):
#       result = {}  # Initialize an empty dictionary
#       for number in numbers:  # Iterate over each number in the input list
#         result[str(number)] = number**2  # Convert number to string and use it as key, set the value as number squared
#       return result  # Return the resulting dictionary
# print(numbers_to_dict([1,2,3]))

# Funtion to return the first and last parameter in the Arguments

# def first_last_parameter(*args):
#     return args[0], args[-1]
# print(first_last_parameter(1,2,3,4,5))

# Function to check whether String is SpongeCase or not
# def is_Spongecase(s):
#    if s == s.lower():
#         return False
#    elif s == s.upper():
#         return False
#    elif s == s.capitalize():
#         return False
#    else:
#         return True  
# print(is_Spongecase("Spongecase"))   

# Function to repeat the last Characters in the String N times
# def repeat_last_char(string,n):
#     return string+string[-1]*n
# print(repeat_last_char("Spongecase",3))

#Function to return longest subsequence in a binary string
# def longest_zero_sequence(binary_string):
#     print(binary_string.split('1'))
#     return len(max(binary_string.split('1')))
# print(longest_zero_sequence('10100100010001'))

#Function to return pencil which has longlead   
# def switch_pencil(pencil1, pencil2):
#         pencil1 = int(pencil1)
#         pencil2 = int(pencil2)
#         # Compare the lengths and return the appropriate string
#         if pencil1 > pencil2:
#             return "pencil 1"
#         else:
#             return "pencil 2" 
   
# print(switch_pencil("3","5"))  

#Function to check given number is a perfect cube and square
# def is_cubic_square(n):
#     Square_of_n = False
#     cube_of_n = False
#     i = 1
#     while i <= n:
#         if (i*i == n):
#             Square_of_n = True
#         if (i*i*i == n):
#             cube_of_n = True
#         i += 1
#     return (Square_of_n and cube_of_n )
# print(is_cubic_square(125))

#Function to return the number that occurs twice and the number which is missing
def find_mismatch(nums):
    x = list(nums)
    n = len(x)
    
    expected_sum = n *(n + 1)/2
    actual_sum = sum(x)
 
    for i in range(0, len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                duplicate = x[i]
                break
    missing = int(expected_sum - (actual_sum - duplicate))
    return [duplicate,missing]                       
print(find_mismatch([1,2,2,4]))            
                
            
        


   
    
    
    
  