# def is_pronic(n):
#     for i in range(1,n+1):
#         if i*(i+1)==n:
#             print(i*(i+1))
#             return True
#     return False
# print(is_pronic(6))


#Broken KeyBoard
# def can_type(keys, word):
#     keys = sorted(keys)
#     word = sorted(word)
#     return keys == word
# print(can_type('abc','bac'))

#Mask Credit card
# def mask_credit_card(card_number):
#     card_number = str(card_number)
#     new_cn = '*' * (len(card_number)-4) + card_number[-4:]
#     return new_cn
# print(mask_credit_card(4444444444444444))

#Hard Question
# def is_disarium_number(num):
#     num1 = str(num)
#     sum_chars = 0
#     for chars in range(len(num1)-1,-1,-1):
#         sum_chars = int(num1[chars])**(chars+1) + sum_chars
#     if str(sum_chars) == num1:
#         return True
#     else:
#         return False
# print(is_disarium_number(518))

#Hard Word Segmentation
# def can_segment_string(words):
#     s2 = " ".join(words)
#     return s2
# print(can_segment_string(words = ['apple', 'pear', 'pier', 'pie']))

#Spongcase letter
# def sponge_case(text):
#     result = []
#     count = 1
#     for i in text:
#         if i == ' ':
#             result.append(i)
#         elif count % 2 == 0:
#             result.append(i.upper())
#             count += 1
#         else:
#             result.append(i.lower())
#             count += 1
#     return ''.join(result)
# print(sponge_case('PROGRAMIZPRO123'))

# Hit JackPot
# def check_jackpot(slot_machine_outcome):
#     return len(set(slot_machine_outcome))==1
# print(check_jackpot(['@','@','@','@']))

# count Even and Odd digits
# def count_digits(n):
#     count_even = 0
#     count_odd = 0
#     for nums in str(n):
#         if int(nums)%2==0:
#             count_even +=1
#         elif int(nums)%2!=0:
#             count_odd +=1
#         else:
#             return "No even and Odd numbers"
#     return count_even,count_odd
# print(count_digits(123456789))

#Numeric SeeSaw
# def numeric_seesaw(n):
#     Range = range(1, n + 1)
#     a= list(Range)
#     for nums in range(n-1,0,-1):
#         a.append(nums)
#     return a
# print(numeric_seesaw(5))

#Find all divisors of n
# def find_divisors(n):
#     divisors = []
#     for i in range(1,n+1):
#         if n%i==0:
#             divisors.append(i)
#     return divisors
# print(find_divisors(12))

#Split Item Code
# def split_item_codes(item_code):
#     return item_code.split('-')
# print(split_item_codes('ABC-123-XYZ'))

#length of the pin
# def validate_pin(pin):
#     if len(pin)==4 or len(pin)==6:
#         return True
#     else:
#         return False
# print(validate_pin('123456'))

# ASCII dictionary
# def ascii_dictionary(string):
#     dictionary = {}
#     for char in string:
#         key = char
#         value = ord(key)
#         dictionary.update({key:value})
#     return dictionary
# print(ascii_dictionary('abc'))

#Get_min_key
# def get_min_key(dict1):
#     if not dict1:
#         return None
#     min_value = min(dict1.values())
#     for key, value in dict1.items():
#         if value == min_value:
#             return key
# print(get_min_key({'a':1,'b':2,'c':3}))

#Number with same Parity
# def check_parity(number):
#     number = str(number)
#     s = 0
#     for nums in number:
#         s = s + int(nums)
#     if s%2==0 and int(number)%2==0:
#         return True
#     elif s%2==1 and int(number)%2==1:
#         return True
#     else:
#         return False
# print(check_parity(243))

#Dict
# def max_pairs(n):
#     d=dict()
#     for i in range(1,n+1):
#         d[str(i)]=i*2
#     return d
# print(max_pairs(5))

#Censor Words
# def censor_words(sentence):
#     x = sentence.split(" ")
#     censor_sentence = ' '
#     for i in range(0,len(x)):
#         if len(x[i])>4:
#             x[i]=len(x[i]) * '*'
#     return censor_sentence.join(x)
# print(censor_words('the quick brown fox jumps over the lazy dog'))

#Product of the list excluding the index of its own
# def self_prod(nums):
#     if len(nums) == 1:
#         return []
#     product = 1
#     for i in nums:
#         product *= i
#     result = []
#     for i in nums:
#         result.append(product // i)
#     return result
# print(self_prod([1,2,3,4]))

#Find the missing letter in the Sequence
# def find_missing_letter(s):
#     f = ord(s[0])
#     l = ord(s[-1])
#     for i in range(f,l):
#         if chr(i) not in s:
#             return chr(i)
# print(find_missing_letter('abcdfg'))

#Prime Diagonal
# def is_prime_diagonal(matrix):
#     def is_prime(num):
#         if num <= 1:  # Numbers <= 1 are not prime
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for i in range(len(matrix)):
#         if not is_prime(matrix[i][i]):  # Check only diagonal elements
#             return "Not Prime Number"
#     return "Yes"
# print(is_prime_diagonal([[2,0],[0,5]]))

#Total Time for Journey
# def car_timer(times):
#     return sum(times)
# print(car_timer([10,20,30]))

#diff b/w two colors using Euclidean Formula
# import math
# def color_difference(color1, color2):
#     one = color1[0]- color2[0]
#     two = color1[1]-  color2[1]
#     three = color1[2]- color2[2]
#     E_D = math.sqrt((one**2) + (two**2) + (three**2))
#     return round(E_D,2)
# print(color_difference((255,255,255),(0,0,0)))

#Calculate the area of in-circle and circum-circle
# import math
# def calculate_circle_areas(square_area):
#     a=math.sqrt(square_area)
#     b=math.sqrt(2*a*a)
#     return (round(math.pi*(a/2)*(a/2),2),round(math.pi*(b/2)*(b/2),2))
# print(calculate_circle_areas(25))

#line_length
# import math
# def calculate_line_length(point1, point2):
#     first_equation = point2[0]-point1[0]
#     print(first_equation)
#     second_equation = point2[1]-point1[1]
#     print(second_equation)
#     length = math.sqrt(first_equation**2 + second_equation**2)
#     return round(length,2)
# print(calculate_line_length((15,7),(22,11)))

#Mersene_primes
# def mersenne_primes(n):
#     l1=[]
#     l2=[]
#     for i in range (2,50):
#         m=2**i-1
#         if m<n:
#             l1.append(m)
#     for i in l1:
#         c=0
#         for j in range(2,i):
#             if i % j==0:
#                 c+=1
#             else:
#                 c+=0
#         if c==0:
#             l2.append(i)
#     return l2
# print(mersenne_primes(130))

#Composite Number
# def is_composite(n):
#     count = 0
#     for i in range(2,n):
#         if n%i==0:
#             count += 1
#     if count>=1:
#         return True
#     else:
#         return False
# print(is_composite(4))

#Weird Number
# def is_weird(n):
#     if n % 2 != 0:
#         return "Weird"
#     elif n % 2 == 0 and 2 <= n <= 5:
#         return "Not Weird"
#     elif n % 2 == 0 and 6 <= n <= 20:
#         return "Weird"
#     elif n % 2 == 0 and n > 20:
#         return "Not Weird"

# Replace Chars
# def replace_chars(string, replacements):
#     for i in replacements:
#         string=string.replace(i,replacements[i])
#     return string
# print(replace_chars('goodbye',{'g':'b','o':'a','d':'y'}))

# Frog Jump
# def frog_jump(numbers):
#     jumps=0
#     curr_num=numbers[0]
#     for j in numbers:
#         if j>curr_num:
#             curr_num=j
#             jumps+=1
#     return jumps
# print(frog_jump([2,1,3,4]))

# Two friends Meet
# def meeting_time(friend1, friend2):
#     start_time1, speed1 = friend1
#     start_time2, speed2 = friend2
#
#     # Calculate the time difference between the friends
#     time_difference = abs(start_time2 - start_time1)
#
#     # Calculate the meeting time
#     meeting_time = time_difference / (speed1 + speed2)
#
#     return round(meeting_time, 2)
#
# print(meeting_time((2,3),(3,2)))

# Last digit of a number in a list
# def end_letters(numbers):
#     last_digits = []
#     for i in  range(0,len(numbers)):
#         last_digits.append(str(numbers[i]%10))
#     return str(last_digits)
# print(end_letters([123,456,789]))

# Johny is making process or not
# def is_johnny_making_progress(day1, day2, day3):
#     if (day2>day1) and (day3>day2):
#         return True
#     else:
#         return False
# print(is_johnny_making_progress(1,2,3))

# convert List to Dict
# def lists_to_dict(list1, list2):
#     listToDict = {}
#     for i in range(len(list1)):
#         listToDict[list1[i]] = list2[i]
#     return listToDict
# print(lists_to_dict(['a','b','c'],[1,2,3]))

#Add the Values of symbols in Matrix
# def add_matrix_values(matrix):
#     s = matrix[0][0]
#     for x in matrix:
#         if '+' in x:
#             s += x[-1]
#         elif '-' in x:
#             s -= x[-1]
#         elif '*' in x:
#             s *= x[-1]
#         elif '/' in x and x!=0:
#             s /= x[-1]
#     return s
# print(add_matrix_values([[1, '+', 2], ['-', 3], ['*', 2]]))

#Count Likes and Dislikes
# def count_votes(votes):
#     vote_counts = {'likes': 0, 'dislikes': 0}
#     for vote in votes:
#         if vote == 'like':
#             vote_counts['likes'] += 1
#         elif vote == 'dislike':
#             vote_counts['dislikes'] += 1
#     return vote_counts
# print(count_votes(['like','dislike','like','like']))

# number with a Thousand Seperator
# def format_number(n):
#     s = ''
#     i = 0
#     while n:
#         if i != 3:
#             s += str(n % 10)
#             n //= 10
#             i += 1
#         else:
#             s += ','
#             i = 0
#     return s[::-1]
# print(format_number(1000000))

# Number is Prime or Not
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         else:
#             return True
# print(is_prime(5))

# Sort Books Based on Author
# def sort_books(books):
#     return sorted(books, key=lambda x: x["author"])

# Count Leap Years in the Range
# def count_leap_years(start_year, end_year):
#     leapYearCount = 0
#     for i in range(start_year,end_year+1):
#         if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
#             leapYearCount += 1
#     return leapYearCount
# print(count_leap_years(2000,2020))

# Numeric SeeSaw
# def numeric_seesaw(n):
#     seeSawList = []
#     for i in range(1,n+1):
#         seeSawList.append(i)
#     for i in range(n-1,0,-1):
#         seeSawList.append(i)
#     return seeSawList
# print(numeric_seesaw(5))

# Pan Digital
# def is_pandigital(n):
#     numString = str(n)
#     for i in range(0,10):
#         if str(i) in numString:
#             return True
#         return False
# print(is_pandigital(1234567890))

#Diagonnaly Dominannt
# def is_diagonally_dominant(matrix):
#     n = len(matrix)
#     for i in range(n):
#         row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
#         if abs(matrix[i][i]) < row_sum:
#             return False
#     return True
# matrix = [
#     [3, -1, 1],
#     [1, 7, 1],
#     [2, -3, 9]
# ]
# print(is_diagonally_dominant(matrix))  # Output: True

# Find the missing Positive number
# def find_missing(numbers):
#     # Consider only positive numbers
#     positives = [num for num in numbers if num > 0]
#     positives = sorted(set(positives))  # Remove duplicates and sort
#     smallest_missing = 1  # Start checking from 1
#
#     for num in positives:
#         if num == smallest_missing:
#             smallest_missing += 1  # Increment if the number is present
#         elif num > smallest_missing:
#             break  # Gap found, smallest_missing is the answer
#
#     return smallest_missing
# print(find_missing([7,8,9,11,12]))

# Find Adjacent
# def find_adjacent_nodes(graph, node):
#     for i in range(1,len(graph)):
#         return graph[str(node)]
# print(find_adjacent_nodes({'1':['2','3'],'2':['1','3'],'3':['1','2']},1))

# Even and Odd Partition
# def even_odd_partition(numbers):
#     even_list = []
#     odd_list = []
#     for num in numbers:
#         if num%2==0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#     return even_list,odd_list
# print(even_odd_partition([1,2,3,4,5]))

# Function to generate nth carol number
# def carol_number(n):
#   return (2**n-1)**2-2
# print(carol_number(3))

# Swap keys and Values of a Dictionary
# def swap_dictionary(dict1):
#     dictSwap = {}
#     for keys,values in dict1.items():
#         dictSwap[values]=keys
#     return dictSwap
# print(swap_dictionary({'a':1,'b':2,'c':3}))

# Generate Combinations
# from itertools import combinations
# def generate_combinations(lst, n):
#     possibleCombinations = combinations(lst,n)
#     return list(possibleCombinations)
# print(generate_combinations(['a','b','c','d'],2))

# Matrix To String
# def matrix_to_string(matrix):
#     globalstring = ""
#     for i in range(0, len(matrix)):
#         for i1 in matrix[i]:
#             globalstring += i1
#     return globalstring
# print(matrix_to_string([['h','e','l','l','o'],['w','o','r','l','d']]))

# numbers in a list are Prime
# def all_primes(numbers):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for number in numbers:
#         if not is_prime(number):
#             return False
#     return True
#
# print(all_primes([29, 31, 36, 37]))

# Get Values from Dictionary
# def get_dictionary_values(dict1):
#     dictValues = []
#     for keys,values in dict1.items():
#         dictValues.append(values)
#     return dictValues
# print(get_dictionary_values({'a':1,'b':2,'c':3}))

# Split based on Capital letter
# def capital_split(s):
#     lst = []
#     for i in range(len(s)):
#         if s[i].isupper():
#             for j in range(i+1, len(s)):
#                 if s[j].isupper():
#                     lst.append(s[i:j])
#                     break
#                 if s[-1] == s[j]:
#                     lst.append(s[i:])
#     return lst
# print(capital_split('heLloWorld'))

# Fulcrum of the List
# def find_fulcrum(lst):
#     for i in range(len(lst)):
#         left_sum = sum(lst[:i])
#         right_sum = sum(lst[i + 1:])
#
#         if left_sum == right_sum:
#             return lst[i]
#     return 'None'
# print(find_fulcrum([7,-1,0,-1,7]))

# Another Solution for Fulcrum
# def find_fulcrum(lst):
#     total_sum = sum(lst)
#     left_sum = 0
#
#     for i in range(len(lst)):
#         right_sum = total_sum - left_sum - lst[i]
#         print(right_sum)
#         if left_sum == right_sum:
#             return lst[i]
#         left_sum += lst[i]
#     return None
# print(find_fulcrum([7,-1,0,-1,7]))

# Count the Digits
# def count_digits(n):
#     digiCount = []
#     while n>0:
#         digiCount.append(n%10)
#         n = n//10
#     return len(digiCount)
# print(count_digits(1000))

# Find the intersection of two intervals
# def intersect_intervals(interval1, interval2):
#     a,c = interval1
#     b,d = interval2
#     start = max(a,b)
#     end = min(c,d)
#     if start <= end:
#         return [start,end]
#     else:
#         return 'None'
# print(intersect_intervals([1,3],[5,7]))

# Find Given number is Ugly or Not
# def is_ugly(number):
#     if number <= 0:
#         return False
#     for factor in [2, 3, 5]:
#         while number % factor == 0:
#             number //= factor
#             print(number)
#     return number == 1
# print(is_ugly(6))
# print(is_ugly(14))


#Find Median from an integer List
# def find_median(nums1, nums2):
#     s1 = sorted(nums1)
#     s2 = sorted(nums2)
#     merged_list = []
#     i = j = 0
#     while i < len(s1) and j < len(s2):
#         if s1[i] < s2[j]:
#             merged_list.append(s1[i])
#             i += 1
#         else:
#             merged_list.append(s2[j])
#             j += 1
#     merged_list.extend(s1[i:])
#     merged_list.extend(s2[j:])
#     if len(merged_list)%2==1:
#         return merged_list[len(merged_list)//2]
#     else:
#         mid1 = merged_list[len(merged_list)//2 - 1]
#         print(mid1)
#         mid2 = merged_list[len(merged_list)//2]
#         print(mid2)
#         return (mid1+mid2)/2
# print(find_median([1,2],[3,4]))

# Filter Positives
# def filter_positives(lst):
#     positive_list = []
#     for num in lst:
#         if num>0:
#             positive_list.append(num)
#     return positive_list
# print(filter_positives([5,3,-2,1,0]))

#Arthimetic Dictionary
# def arithmetic_operations(a,b):
#     arithmetic_operations_dict = {}
#     stringList = ['Addition','Subtraction','Multiplication','Division']
#     arithmetic_operations_dict = {stringList[0]:a+b,
#                                   stringList[1]:a-b,
#                                   stringList[2]:a*b,
#                                   stringList[3]:a/b
#                                  }
#     return arithmetic_operations_dict
# print(arithmetic_operations(5,2))

#Closet Points to Origin (0,0)
# import math
# def closest_points(points_list,k):
#     distances = [(math.sqrt(x**2 + y**2), (x, y)) for x, y in points_list]
#     distances.sort()
#     closest_k_points = [point for _, point in distances[:k]]
#     return closest_k_points
# print(closest_points([(1,3),(-2,2)],1))

# Broken KeyBoard
# def can_type(keys, word):
#     for w in word:
#         if w not in keys:
#             return False
#     return True
# print(can_type('abcdefg','bag'))

# Two List Intersection
# def lst_intersection(nums1, nums2):
#     a = set(nums1)
#     b = set(nums2)
#     return sorted(a & b)
# print(lst_intersection([1,2,3,4],[4,3,5]))

#


            
