# def is_pronic(n):
#     for i in range(1,n+1):
#         if i*(i+1)==n:
#             print(i*(i+1))
#             return True
#     return False
# print(is_pronic(6))
from numpy.ma.core import count


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







            
