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
def car_timer(times):
    return sum(times)
print(car_timer([10,20,30]))
