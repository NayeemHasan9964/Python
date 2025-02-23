# Retrieve last n numbers from a List
# def retrieve_last_elements(lst,n):
#     if n<=0:
#         return []
#     return lst[-n:]
# print(retrieve_last_elements([1,2,3,4,5],2))

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

# Euclid Number
# def euclid_number(n):
#     p = 1  # Initialize product
#     count = 0  # Count of prime numbers found
#     num = 2  # Start checking for primes from 2
#
#     while count < n:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 break
#         else:  # If no break occurred, num is prime
#             p *= num  # Multiply prime number to product
#             count += 1
#         num += 1  # Check the next number
#
#     return p + 1  # Return the Euclid number
# print(euclid_number(5))

# RowSum
# def row_sum(matrix):
#     rowSum = []
#     for i in range(0,len(matrix)):
#         rowSum.append(sum(matrix[i]))
#     return rowSum
# print(row_sum([[1,2],[3,4]]))

# Calculate Salary
# def calculate_salary(hours):
#
#     if hours <= 40:
#         return hours * 20
#     else:
#         afterFourtyHours = hours - 40
#         afterFourtyHourSalary = afterFourtyHours * 25
#
#         FirstFourtyHours = hours * 20
#         FinalSalary = FirstFourtyHours - (afterFourtyHours * 20)
#         TotalSalary = FinalSalary + afterFourtyHourSalary
#         return TotalSalary
# print(calculate_salary(35))

# Extend Vowel in String
# def extend_vowels(word, n):
#     vowelString = []
#     vowels = 'aeiouAEIOU'
#     for char in word:
#         if char in vowels:
#             vowelString.append(char * n)
#         else:
#             vowelString.append(char)
#     return ''.join(vowelString)
# print(extend_vowels('hello', 3))

# Common Elements
# def common_elements(set1, set2):
#     commonElements = set1 & set2
#     if len(commonElements) == 0:
#         return None
#     else:
#         return commonElements
# print(common_elements({1,2,3},{4,5,6}))

# Powerful number or Not
# def is_powerful(n):
#     prime_factors = set()
#     num = n
#     for i in range(2, n + 1):
#         while num % i == 0:
#             prime_factors.add(i)
#             num //= i
#         if num == 1:
#             break
#
#     for p in prime_factors:
#         if n % (p * p) != 0:
#             return False
#
#     return True
# print(is_powerful(16))

# Move Capital Letters to Front
# def move_capitals_to_front(s):
#     upperString = ""
#     lowerString = ""
#     for char in s:
#         if char.isupper():
#             upperString = upperString + char
#         elif char.islower():
#             lowerString = lowerString + char
#     return upperString+lowerString
# print(move_capitals_to_front('HelloWorld'))

# import math
# def calculate_distance(point1, point2):
#     x1,y1 = point1
#     x2,y2 = point2
#     distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     print(x2-x1)
#     print(y2-y1)
#     return round(distance,2)
# print(calculate_distance([1,2],[4,5]))

# Rock Paper scissors Game
# def rock_paper_scissors(player1_choice, player2_choice):
#
#     r = "rock"
#     p = "paper"
#     s = "scissors"
#     if player1_choice == r and player2_choice == p:
#         return "player 2 wins"
#     elif player1_choice == p and player2_choice == r:
#         return "player 1 wins"
#     elif player1_choice == p and player2_choice == s:
#         return "player 2 wins"
#     elif player1_choice == s and player1_choice == p:
#         return "player 1 wins"
#     elif player1_choice == s and player2_choice == r:
#         return "player 2 wins"
#     elif player1_choice == r and player2_choice == s:
#         return "player 1 wins"
#     elif player1_choice == r and player2_choice == r:
#         return "tie"
#     elif player1_choice == p and player2_choice == p:
#         return "tie"
#     elif player1_choice == s and player2_choice == s:
#         return "tie"
#
# print(rock_paper_scissors("rock","rock"))

# Sum of Letters
# def sum_of_letters(string):
#     ASCIIValues = []
#     for char in string:
#         ASCIIValues.append(ord(char))
#     valueSum = sum(ASCIIValues)
#     if valueSum % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
# print(sum_of_letters('abc'))

# Nearest Element in the list
# def nearest_element(numbers, target):
#     if target <= 0:
#         return "Enter a number greater than zero"
#
#     closest = None  
#     min_difference = float('inf')
#
#     for num in numbers:
#         difference = abs(num - target)
#         if difference < min_difference:
#             min_difference = difference
#             closest = num
#
#     return closest
# print(nearest_element([7,11,13],8))

# Jacobsthal number
# def jacobsthal(n):
#     j = [0, 1]
#     for i in range(1, n):
#         j.append(j[i] + (2 * j[i - 1]))
#     return j[-1]
#
# print(jacobsthal(6))

# In Recursive
# def jacobsthal(n):
#     if n < 2:
#      return n
#
#     return jacobsthal(n - 1) + 2 * jacobsthal(n - 2)
# print(jacobsthal(6))

# Odd Sum
# def sum_of_odds(numbers):
#     oddList = [num for num in numbers if num%2 != 0]
#     return sum(oddList)
# print(sum_of_odds([1,2,3,4,5]))

# Rhythm Syncopated
# def is_syncopated(rhythm):
#     r =list(rhythm)
#     for char in r:
#         if char == ' ':
#             return "Yes"
#     return "No"
# print(is_syncopated("+++ +++"))

# Vertex of quadratic
# def vertex(a,b,c):
#     if a==0:
#         return None
#     x=-b/(2*a)
#     y=((4*a*c)-(b**2))/(4*a)
#     return x,y
# print(vertex(1,-3,2))

# Words are anagrams with their ASCII values anagrams after Squaring
# def anagramic_squares(word1, word2):
#     a  = sorted(word1) == sorted(word2)
#     s1 = [ord(i) for i in word1]
#     s2 = [ord(i) for i in word2]
#     return a and sorted(s1) == sorted(s2)
# print(anagramic_squares('cat','tac'))

# List contains three consecutive common numbers
# def check_consecutive_numbers(numbers):
#     countCommon = 0
#     i = 0
#     j = len(numbers)-1
#     while i<len(numbers):
#         if numbers[i] == numbers[j]:
#             countCommon += 1
#         i = i + 1
#         j = j - 1
#     print(countCommon)
#     if countCommon == 3:
#         return True
#     else:
#         return False
# print(check_consecutive_numbers([1,2,2,3]))

# Pile up cubes vertically
# def pile_up_cubes(cubes):
#     n = sorted(cubes)
#     if n[::-1] == cubes:
#         return "Yes"
#     else:
#         return "No"
# print(pile_up_cubes([5,4,3,2,1]))

# Valid CheckPost
import re

from pyparsing import alphas


# def validate_postal_code(code):
#     if len(code)>6:
#         return "Invalid Code"
#     for i in range(len(code) - 1):
#         if code[i] == code[i + 1]:
#             return False
#     return True
# print(validate_postal_code('121426'))

# Blum Integer
# def is_blum_integer(n):
#     PrimeNumbers = []
#     for num in range(2,n):
#         if num > 1:
#             for i in range(2,num):
#                 if num % i == 0:
#                     break
#             else:
#                 PrimeNumbers.append(num)
#     print(PrimeNumbers)
#     for p in range(0,len(PrimeNumbers)):
#         for  q in range(p+1,len(PrimeNumbers)):
#             if (p * q == n  or  p * p == n) and (p % 4 == 3 and q % 4 == 3):
#                 return True
#     return False
# print(is_blum_integer(15))

# Replace letter with a string of its position with number
# def replace_with_position(s):
#     numList = []
#     alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
#     for char in s:
#         for key, value in alphabet_dict.items():
#             if char == key:
#                 numList.append(str(value))
#     return ' '.join(numList)
# print(replace_with_position('hello'))

# Extract Domain
# def extract_domain(url):
#     if not url:  # Handle empty input
#         return ""
#  # Remove protocol (http:// or https://)
#     if "://" in url:
#         url = url.split("://", 1)[1]
#  # Remove 'www.' if present
#     if url.startswith("www."):
#         url = url[4:]
# # Extract only the domain (before any `/` or `?`)
#     url = url.split('/')[0]  # Remove path
#     url = url.split('?')[0]  # Remove query parameters
#     return url
# print(extract_domain('https://www.google.com'))

# Mountain List
# def is_mountain(lst):
#         if lst[-1] != max(lst):
#             if lst[0] != max(lst):
#                 return True
#         return False
# print(is_mountain([0,3,2,1]))

# Explosion Intensity
# def explosion_intensity(s):
#     intensity = ''
#     for char in range(0,len(s)):
#         intensity = intensity + (s[char] * (char+1))
#     return intensity
# print(explosion_intensity('Boom'))

# n-List differences
# def n_differences(lst):
#     lst2=lst
#     while len(lst2)!=1:
#         lst1=[]
#         for i in range(1,len(lst2)):
#             lst1.append(lst2[i]-lst2[i-1])
#         lst2=lst1
#     return lst2[0]
# print(n_differences([5,2,1]))

# Special List
# def is_special(lst):
#     for index in range(len(lst)):
#         if (index % 2 == 0) and (lst[index] % 2 == 0):
#                 return True
#         if (index % 2 != 0) and (lst[index] % 2 != 0):
#                 return  True
#         else:
#                 return False
# print(is_special([2,5,4,3,6,1]))

# Digit Distance
# def digit_distance(num1, num2):
#     n1 = list(num1)
#     n2 = list(num2)
#     n3 = []
#     for i in range(0,len(n1)):
#         n3.append(abs(int(n2[i]) - int(n1[i])))
#     return sum(n3)
# print(digit_distance('11111','22222'))

# Primorial Number
# def calculate_primorial(n):
#     primeList = []
#     primeMul = 1
#     for num in range(2,n+1):
#         if num > 1:
#             for i in range(2,num):
#                 if num % i == 0:
#                     break
#             else:
#                 primeList.append(num)
#     for num in primeList:
#         primeMul = primeMul * num
#     return primeMul
# print(calculate_primorial(5))

# Broken Keyboard
# def type_with_broken_keyboard(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     string = ""
#     bool = 0
#     for char in word:
#         if char in vowels:
#             bool += 1
#         if bool % 2 == 1:
#             string += char.upper()
#             continue
#         string += char
#     return string
# print(type_with_broken_keyboard('banana'))

# Abbreviate the Sentence
# def abbreviate_sentence(sentence):
#     return ' '.join([f'{i[0]}{len(i)}' for i in sentence.split()])
# print(abbreviate_sentence('Hello World'))

# Count Occurrences
# def count_letters(word):
#     countDict ={}
#     for char in word:
#         if char not in countDict:
#             countDict[char] = 1
#         else:
#             countDict[char] += 1
#     return countDict
# print(count_letters('banana'))

# Ma product from a list
# def product_of_largest(numbers):
    # prodList = []
    # for i in range(1,len(numbers)):
    #     prodList.append(numbers[i] * numbers[i-1])
    # print(prodList)
    # return max(prodList)
#     numbers.sort()
#     return numbers[-1] * numbers[-2]
# print(product_of_largest([-10,-20,-30,40]))

# Max number index
# def highest_index(numbers):
#     maxNumber = max(numbers)
#     maxIndex = []
#     for i in range(0,len(numbers)):
#         if numbers[i] == maxNumber:
#             maxIndex.append(i)
#     return max(maxIndex)
# print(highest_index([1,2,3,2,3]))

# Pentagonal Number
# def pentagonal_number(n):
#     return round(n * (3*n-1)/2)
# print(pentagonal_number(5))

















