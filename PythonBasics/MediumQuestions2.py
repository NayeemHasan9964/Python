# Retrieve last n numbers from a List
# def retrieve_last_elements(lst,n):
#     if n<=0:
#         return []
#     return lst[-n:]
# print(retrieve_last_elements([1,2,3,4,5],2))
from xxsubtype import bench

from pandas.core.dtypes.inference import is_re
from pyparsing import countedArray


# Check if given String is in the middle of the other string
# def is_in_center(s1, s2):
#     middleChar = s2[len(s2)//2]
#     if middleChar==s1[0]:
#         return True
#     else:
#         return False
# print(is_in_center('abc','xxabcxx')

# Excuse Threes
# def excuse_threes(n):
#     lst = []
#     for i in range(0,n+1):
#         if i%3==0:
#             continue
#         else:
#             lst.append(i)
#     return lst
# print(excuse_threes(10))

# Max_Score Divisibility
# def max_divisibility_score(n):
#     if n <= 0:
#         return None
#
#     scores = []
#
#     def find_div_score(num):
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         return count
#
#     for num in range(1, n + 1):
#         scores.append(find_div_score(num))
#     print(scores)
#     max_score = max(scores)
#     return scores.index(max_score) + 1
# print(max_divisibility_score(10))

# Prime Factors of a Number
# def prime_factors(n):
#     prime_factors_set = set()
#     divisor = 2
#
#     while n > 1:
#         while n % divisor == 0:
#             prime_factors_set.add(divisor)
#             n //= divisor  # Reduce n
#
#         divisor += 1
#
#     return list(prime_factors_set)
#
# print(prime_factors(56))

# Circular Shift
# def circular_shift(lst):
#     circularLst = [lst[-1]]
#     for i in range(0,len(lst)-1):
#         circularLst.append(lst[i])
#     return circularLst
# print(circular_shift([1,2,3,4,5]))

# Similar items in a list to dictionary
# def group_items(lst):
#     groups = {}
#     for index, item in enumerate(lst):
#         if item not in groups:
#             groups[item] = []
#         groups[item].append(index)
#     return groups
# print(group_items(['apple','banana','apple','banana']))

# Correct a Sentence
# def correct_sentence(sentence):
#     sentence = sentence.strip().capitalize()
#     if sentence[-1] != '.':
#         sentence += '.'
#
#     return f"{sentence.strip()}"
#
# print(correct_sentence('this is a test'))

#Total time spend on Washing Hands
# def total_washing_time(times_per_day, months):
#     oneHandWashInSeconds = 21
#     totalSecondsInADay = oneHandWashInSeconds * times_per_day
#     convertingIntoMinutes = totalSecondsInADay/60
#     totalTimeInMonths = (convertingIntoMinutes * 30) * months
#     totalMinutes = int(totalTimeInMonths)
#     totalSeconds = round((totalTimeInMonths - totalMinutes) * 60)
#     return f"{totalMinutes} minutes and {totalSeconds} seconds"
# print(total_washing_time(5,3))

# Check value is in Dict or not
# def value_exist(dict1, val):
#     for values in dict1:
#         if dict1[values]==val:
#             return True
#     return False
# print(value_exist({'a':1,'b':2},1))

# Triple Function
# def triple_function(a,b,c):
#     if a == True and b == True and c == True:
#         return True
#     else:
#         return False
# print(triple_function(True,False,True))

# String can be obtained from another string
# def is_long_pressed(name, typed):
#     name_list = list(name)
#     name_typed = list(typed)
#     for i in range(0, len(typed)):
#         if name_list[i] == name_typed[i]:
#             continue
#         else:
#             name_list.insert(i,name_typed[i])
#     return name_list==name_typed
# print(is_long_pressed("alex","aaleex"))

# Pronounce of X,s
# def pronounce_xs(s):
#     vowels = 'aeiouAEIOU'
#     result = []
#     i = 0
#
#     while i < len(s):
#         if s[i] == 'x':
#             if i + 1 < len(s) and s[i + 1] in vowels:
#                 result.append("cks")
#             else:
#                 result.append("k")
#         else:
#             result.append(s[i])
#         i += 1
#
#     return ''.join(result)
# print(pronounce_xs("xerox"))

# convert a color from CMYK format to RGB format
# def cmyk_to_rgb(cmyk):
#     c,m,y,k =  cmyk
#     R = 255 * (1-c)*(1-k)
#     G = 255 * (1-m)*(1-k)
#     B = 255 * (1-y)*(1-k)
#     return round(R),round(G),round(B)
# print(cmyk_to_rgb([0.4,0.49,0.552,0.36]))

# heterogeneous Dict
# def filter_dict(d):
#     result = {key: value for key, value in d.items() if isinstance(value, int)}
#     return result
# print(filter_dict({'a':1,'b':'2','c':3.0,'d':[4],'e':5}))

# reverse vowels in a string
# def reverse_vowels(S):
# #     vowels = 'aeiouAEIOU'
# #     S = list(S)
# #     i, j = 0, len(S) - 1
# #
# #     while i < j:
# #         if S[i] not in vowels:
# #             i += 1
# #         elif S[j] not in vowels:
# #             j -= 1
# #         else:
# #             S[i], S[j] = S[j], S[i]
# #             i += 1
# #             j -= 1
# #
# #     return ''.join(S)
# #
# # print(reverse_vowels('pperu'))

# Maximize first number
# def maximize_first_number(numbers):
#     result = []
#     a, b = numbers
#     max_number = int("".join(sorted(str(a), reverse=True)))
#     result.append(max_number)
#     result.append(b)
#
#     return result
# print(maximize_first_number([9876,12345]))

# LCM of two numbers
# import  math
# def calculate_lcm(num1,num2):
#     lcm = abs(num1*num2)//math.gcd(num1,num2)
#     return lcm
# print(calculate_lcm(12,15))

# Straight line or not
# def check_straight_line(coordinates):
#
#     x1, y1 = coordinates[0]
#     x2, y2 = coordinates[1]
#
#     dx, dy = x2 - x1, y2 - y1
#     print(dx,dy)
#
#     for i in range(1, len(coordinates) - 1):
#         x1, y1 = coordinates[i]
#         x2, y2 = coordinates[i + 1]
#
#
#         if (y2 - y1) * dx != (x2 - x1) * dy:
#             return False
#
#     return True
#
# # Example usage
# print(check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]))
# print(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6]]))

# Abundant number
# def is_abundant(n):
#     divisors = []
#     sumOfDivisors = 0
#     for i in range(1,n):
#         if n%i == 0:
#             divisors.append(i)
#     for nums in divisors:
#         sumOfDivisors = sumOfDivisors + nums
#     if sumOfDivisors > n:
#         return True
#     else:
#         return False
# print(is_abundant(6))

# Filter Positive Numbers
# def positive_filter(numbers):
#     positive_numbers = [i for i in numbers if i>0]
#     return positive_numbers
# print(positive_filter([-1,2,-3,4,-5]))

# is Prime or not
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# # print(is_prime(3))

# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     else:
#         print(i,end = " ")
#         i += 1

# print('The sum of {0} and {1} is {2}'.format(2, 10, 12))

# First repeating Digit
# def findFirstRepeatingDigit(digitPattern):
#     seen = set()
#
#     for digit in digitPattern:
#         if digit in seen:
#             return digit
#         seen.add(digit)
#
#     return -1
# print(findFirstRepeatingDigit('12342'))

# List is Balanced
# def is_balanced(lst):
#     half = len(lst)//2
#     sum1 = sum(lst[:half])
#     sum2 = sum(lst[half:])
#     if sum1 == sum2:
#         return True
#     else:
#         return False
# print(is_balanced([1,2,3,3,2,1]))

# Replace Characters
# def double_character_swap(text, char1, char2):
#     swapped_text = text.maketrans({char1: char2, char2: char1})
#     return text.translate(swapped_text)
# print(double_character_swap('hello world','h','w'))

# Valid Arithmetic
# def is_math_expression(s):
#     nums = '0123456789'
#     arth_operators = '+-*/()'
#     for char in s:
#         if char in nums or char in arth_operators:
#             continue
#         else:
#             return False
#     return True
# print(is_math_expression('(4+5)*6/7-8'))

# def sequence_type(numbers):
#     first_diff = list()
#     second_diff = set()
#     i = len(numbers)-1
#     j = i - 1
#     while i > 0 :
#         first_diff.append(numbers[i] - numbers[j])
#         i = i - 1
#         j = j - 1
#
#     for i in range(1,len(first_diff)):
#         second_diff.add(first_diff[i] - first_diff[i - 1])
#
#     if len(second_diff) == 1 and 0 in second_diff:
#         return 'Linear'
#     elif len(second_diff) == 1:
#         return 'Quadratic'
#     else:
#         return 'Cubic'
#
#
# print(sequence_type([1,4,9]))

# Extract name from an Email
# def get_name_from_email(email):
#     email = email.split('@')
#     name = email[0]
#     name = name.replace('.',' ')
#     return name
# print(get_name_from_email('john.doe@example.com'))

# Alternating Factorial
# def alternating_factorial(n):
#         def factorial(n):
#             fact = 1
#             for i in range(1, n + 1):
#                 fact *= i
#             return fact
#
#         fact_sum = 0
#         for i in range(1, n + 1):
#             if i % 2 == 0:
#                 fact_sum += factorial(i)
#             else:
#                 fact_sum -= factorial(i)
#         return fact_sum
# print(alternating_factorial(5))

# count number of zeroes in the Binary
# def count_zeroes(n):
#     binArr = []
#     while n > 0:
#         bit = n % 2,
#         binArr.append(str(bit))
#         n //= 2
#     binArr.reverse()
#     binary_num = ''.join(binArr)
#     zero_count = 0
#     for char in binary_num:
#         if char == '0':
#             zero_count += 1
#     return zero_count
# print(count_zeroes(18))

# Convert Keys and Values of Dict to list
# def dict_to_lists(dict):
#     keys = []
#     numbers = []
#     for key,values in dict.items():
#         keys.append(key)
#         numbers.append(values)
#     return keys,numbers
# print(dict_to_lists({'a':1,'b':2,'c':3}))

# Count No of elements in the multidimensional list
# def count_elements(lst):
#     length  = []
#     for i in lst:
#         length.append(len(i))
#     return sum(length)
# print(count_elements([[1,2],[3,4],[5,6]]))
