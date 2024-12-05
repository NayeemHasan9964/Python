# #Function to calculate the BMI of a person
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return round(bmi ,2)
# print(calculate_bmi(78.2,6.2))

# #Function to Reverse a number
# def reverse_number(num):
#     rev_num =  int(str(num)[::-1])
#     if(rev_num > num):
#         return False
#     else:
#         return True
# print(reverse_number(27))

# #Function to find the number of Tallest Candles in a list:
# def find_tallest_candles(candles):
#     max_height = max(candles)
#     count = 0
#     for i in range(len(candles)):
#         if candles[i] == max_height:
#             count += 1
#     return count
# print(find_tallest_candles([5,10,3,14,5,14]))

# #Function to covert a string into camel case letter
# def camel_case(s):
#     words = s.split()
#     return words[0] + ''.join(word.capitalize() for word in words[1:])
# print(camel_case('hello world'))

# #Function to return the total cost of items bought for memorial day
# def memorial_cost(prices):
#     x = prices.split()
#     int_num = [int(num) for num in x]
#     return sum(int_num)
# print(memorial_cost('20 30 40'))

# #Function to return whether it has D_P_integers or Negative
# def positive_dominant(lst):
#     p_count = 0
#     n_count = 0
#     for i in range(0 , len(lst)):
#         if (lst[i] < 0):
#             n_count += 1
#         elif (lst[i] > 0):
#             p_count += 1
#     if (p_count > n_count):
#         return True
#     else:
#         return False
# print(positive_dominant([-1, -1, -2, -3, 4, 4]))

#Function to multiply each number in a list with 2
# def multiply_by_two(numbers):
#     multiplied_list = []
#     for num in numbers:
#         multiplied_list.append(num * 2)
#     return multiplied_list
# print("The multiplied list is:" ,multiply_by_two([1, 2, 3, 4, 5]))

#Function to calculate the points of Scrabble word
# def scrabble_points(word):
#     lower_case = word.lower()
#     sum = 0
#     points = {'a': 1, 'b': 3, 'c': 3,
#                'd': 2, 'e': 1, 'f': 4,
#                'g': 2, 'h': 4, 'i': 1,
#                'j': 8, 'k': 5, 'l': 1,
#                'm': 3, 'n': 1, 'o': 1,
#                'p': 3, 'q': 10, 'r': 1,
#                's': 1, 't': 1, 'u': 1,
#                'v': 4, 'w': 4, 'x': 8,
#                'y': 4, 'z': 10}
#     for char in lower_case:
#        sum += points[char]
#     return sum
# print(scrabble_points('hello'))

#Function to return highest number in a digit
# def highest_digit(n):
#     n_string = str(n)
#     x = list(n_string)
#     return max(x)
# print(highest_digit(12345))

#Function to find all words in a sentence starts with a vowel.
# def find_vowel_words(sentence):
#      vowels ={'a','e','i','o','u'}
#      words = sentence.split()
#      result = [word for word in words if word[0].lower() in vowels]
#      return result
# print(find_vowel_words('I am doing fine'))

#Function to print sum all digits between given two numbers
# def sum_of_digits(start,end):
#     total_sum = 0
#     for num in range(start, end + 1):
#         for digit in str(num):
#             total_sum += int(digit)
#     return total_sum
# print(sum_of_digits(10,15))

#Function to find the length of the line
# import math
# def calculate_line_length(point1, point2):
#     x1,y1 = point1
#     x2,y2 = point2
#     length_of_line = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     return length_of_line

# print(calculate_line_length((2,2),(4,6)))

#Function to check if a given hand poker cards is full house
# def is_full_house(hand):
#      rank_counts = {}

#      for card in hand:
#         rank = card[0]  # Extract the rank of the card (assuming rank is the first character)
#         if rank in rank_counts:
#             rank_counts[rank] += 1
#         else:
#             rank_counts[rank] = 1

#     # Get the counts of each rank
#      counts = list(rank_counts.values())

#     # Check if the hand is a Full House (one 3-of-a-kind and one pair)
#      return sorted(counts) == [2, 3]


# print(is_full_house(['2','2','3','3','3']))

#Function to divide chocolates among the children
# def divide_chocolates(total_chocolates, total_children):
#     list = []
#     no_of_chocolates = list.append(int(total_chocolates / total_children))
#     remaining_chocolates = list.append(int(total_chocolates % total_children))
#     return list

# print(divide_chocolates(15,4))

#Function to remove duplicates from a list
# def remove_duplicates(input_list):
#     return sorted(list(set(input_list)))
# print(remove_duplicates([1,2,2,3,4,4]))

#Funtion find to smallest number in each list from group of lists
# def find_smallest(lists):
#     a,b,c = lists
#     return [min(a),min(b),min(c)]
# print(find_smallest([[1,2,3],[4,5,6],[7,8,9]]))

#Function to replace the  item in a list with a new item,if the item is found in the list
# def replace_item(lst, old_item, new_item):
#     for i in range(0,len(lst)):
#         if lst[i] == old_item:
#             lst.pop(i)
#             lst.insert(i,new_item)
#     return lst
# print(replace_item(['apple','banana','cherry'],'banana','orange'))

#Function to check if a given key exists in a dictionary
# def check_key(dictionary, key):
#     if key in dictionary:
#             return True
#     else:
#             return False
# print(check_key({'name':'John','age':30,'city':'New York'},'age'))

#Function to check if the last item is equal to concatination of other items
# def check_last_item(lst):
#         srt1 = lst[-1]
#         srt2 = ''.join(lst[:-1])
#         if len(lst) > 1:
#                 return srt1 == srt2
#         else:
#                 return False
# print(check_last_item(['a','b','c','abc']))

#Function to find the largert number formed after swapping two digits of a given number
# def largest_swap(num):
#         R_num = 0
#         while num > 0:
#                 num1 = num % 10
#                 R_num = R_num*10 +  num1
#                 num = num // 10
#         if (R_num > num):
#                 return R_num
#         else:
#                 return num
# print(largest_swap(27))

# Fucntion to convert a string to list
# def string_to_list(s):
#         x = s.split()
#         return x
# print(string_to_list("Hello World"))

#Function to check given two lists are equal or not
# def check_lists(lst1, lst2):
#         if lst1 == lst2:
#                 return True
#         else:
#                 return False
# print(check_lists([1,2,3],[1,2,3]))

#Function to calculate the number of trips a driver has to make to transport 12 passengers
# def calculate_trips(seats):
#         if (seats == 0):
#                 return "number of seats cannot be zero"
#         trips = (12 + seats - 1) // seats
#         return trips
# print(calculate_trips(0))

#Function to create a stutterinf effect on a given word
# def stuttering(word):
#         return word[0] +  word[1] + "..." + word[0] + word[1] + "..." + word + "??"
# print(stuttering("hello"))

#Write a function to repeat chars in a string
# def repeat_chars(s, n):
#     return ''.join([char * n for char in s])
# print(repeat_chars('abc', 3))  # Output: hheelllloo

#Write a funtion that returns the list of string
# def loves_me_not(n):
#     x = list()
#     for i in range(1,n+1):
#         if(i%2 == 0):
#             x.append("Loves me not")
#         if(i%2 != 0):
#             x.append("Loves me")
#     return x
# print(loves_me_not(4))

#Write a function to modify a tuple
# def modify_tuple(tupl, elem):
#         x = list(tupl)
#         x .append(elem)
#         return tuple(x)
# print(modify_tuple((1,2,3), 4))

#write a funtion to repeat vowels twice in String
# def repeat_vowels(s):
#     vowels = 'aeiouAEIOU'
#     return ''.join([char * 2 if char in vowels else char for char in s])
# print(repeat_vowels('hello'))  # Output: heellllo

# def find_largest(numbers):
#     return max(numbers)
# print(find_largest([1,2,3,4,5]))

#Write a fucntion that takes floating number and return reverse of that number
# def reverse_number(num):
#     return float(str(num)[::-1])
# print(reverse_number(123.45))


# def remove_vowels(string):
#     vowels = "aeiouAEIOU"
#     print(''.join([char for char in string if char not in vowels]))
# remove_vowels("Hello World")

# To compare the first and last character of string
# def check_chars(s):
#     return s[0]==s[len(s)-1]
# print(check_chars("hello"))

#To check number is within in the Range
# def is_in_range(n, start, end):
#     for i in range(start,end+1):
#         if i==n:
#             return True
#     return False
# print(is_in_range(20,1,20))

# import math
# def calculate_area(radius):
#     Area = math.pi*radius**2
#     return round(Area,2)
# print(calculate_area(5))

# def sum_of_evens(numbers):
#     even_sum = 0
#     for i in range (0,len(numbers)):
#         if numbers[i]%2==0:
#             even_sum = even_sum + numbers[i]
#     return even_sum
# print(sum_of_evens([1,2,3,4,5]))

# def list_union_intersection(list1, list2):
#     union = sorted(set(list1).union(list2))
#     intersection = sorted(set(list1).intersection(list2))
#     return (union, intersection)
# print(list_union_intersection([1,2,3,4],[3,4,5,6]))

# def number_to_reversed_list(n):
#     lst = []
#     while n>0:
#         num = n%10
#         lst.append(num)
#         n = n//10
#     return lst
# print(number_to_reversed_list(12345))

# def count_occurrences(item, tup):
#     n = len(tup)
#     count = 0
#     for i in range(0,n):
#             if tup[i]==item:
#                 count +=1
#     return count
# print(count_occurrences('a',('a','b','c','a','a','a')))

# def sort_by_length(lst):
#     n = len(lst)
#     for i in range (0,n):
#         for j in range(i+1,n):
#             if len(lst[i])>len(lst[j]):
#                 lst[i],lst[j] = lst[j],lst[i]
#     return lst
# print(sort_by_length(["apple","cherry","date","bat"]))

# def frequency_distribution(lst):
#     frequency = {}
#     for item in lst:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#     return frequency
# print(frequency_distribution(['a','b','a','c','b','a']))

# def greet(country):
#     greetings = {'USA':'Hello',
#                 'France':'Bonjour',
#                  'Spain':'Hola',
#                  'Germany':'Hallo',
#                  'Italy':'ciao'}
#     welcome = greetings[country]
#     return welcome
# print(greet('Spain'))

# def to_from_list(n):
#     lst = []
#     if isinstance(n, list):
#         string = str(n)
#         return string
#     if isinstance(n, int):
#         if n == 0:
#             x = str(n)
#             lst.append(int(x))
#             return lst
#         if n>0:
#             while n>0:
#                 lst.append(n%10)
#                 n = n//10
#         return lst[::-1]
# print(to_from_list(0))

# def get_user_info(name, age, address):
#     user_info = { "Name": name,
#                   "Age": age,
#                   "Address": address}
#     return user_info
# print(get_user_info("John",25,"New York"))

# def calculate_power(base, exponent):
#     return base**exponent
# print(calculate_power(2,2))

# def get_union_sum(set1,set2):
#     lst = list(set1.union(set2))
#     sum = 0
#     for num in lst:
#         sum = sum + num
#     return sum
# print(get_union_sum({1,2,3,4},{2,3,4,5}))

# def single_occurrence(s):
#     char= s[0]
#     count = 0
#     for chars in range(0,len(s)):
#         if char == s[chars]:
#             count = count + 1
#     if count>1:
#         return "OccurredTwice"
#     else:
#         return char
# print(single_occurrence("Hello HWorld"))

# def min_removals_for_even_sum(numbers):
# #     current_sum = sum(numbers)
# #     removals = 0
# #     for num in numbers:
# #         if current_sum % 2 == 0:
# #             return removals
# #         current_sum -= num
# #         removals += 1
# #     return removals
# #
# # # Test the function
# # numbers = [7, 9, 11]
# # result = min_removals_for_even_sum(numbers)
# # print(f"Minimum removals to get an even sum: {result}")

# def reverseArray(lst):
#     rv =[]
#     for i in range(len(lst)-1,-1,-1):
#         rv.append(lst[i])
#     return rv
#
# print(reverseArray([1,4,3,2]))

# def fizzBuzz(n):
#     for i in range(1,n):
#         if i%3==0 and i%5==0:
#             print('FizzBuzz')
#         elif i%3==0:
#             print('Fizz')
#         elif i%5==0:
#             print('Buzz')
#         else:
#             print(i)
# print(fizzBuzz(20))

# def decrypt_password(encrypted_password):
#     decrypted_password = ""  # To store the result
#     i = 0
#     temp_number = ""  # To store numbers temporarily
#
#     while i < len(encrypted_password):
#         if i + 1 < len(encrypted_password) and encrypted_password[i].islower() and encrypted_password[i + 1].isupper():
#             # Rule 2: Swap lowercase and uppercase, add '*'
#             decrypted_password += encrypted_password[i + 1] + encrypted_password[i] + '*'
#             i += 2  # Move to the next pair
#         elif encrypted_password[i].isdigit():
#             # Rule 3: Replace number with 0 and place number at the start
#             temp_number += encrypted_password[i]  # Store the number
#             decrypted_password += '0'
#             i += 1  # Move to the next character
#         else:
#             # Rule 4: No modification, just add the character
#             decrypted_password += encrypted_password[i]
#             i += 1  # Move to the next character
#
#     # Prepend the collected numbers to the result
#     decrypted_password = temp_number + decrypted_password
#
#     return decrypted_password
#
#
# # Example usage
# encrypted = "hAck3rr4nk"
# result = decrypt_password(encrypted)
# print(result)  # Output: "43Ah*ck0rr0nk"

def first_n_vowels(string, n):
    vowels = "aeiouAEIOU"
    count = 0
    lst = []
    for char in string:
        if char in vowels:
            count += 1
            lst.append(char)
    if count < n:
        return "Not found"
    else:
        return lst
print(first_n_vowels('Hello World',3))















