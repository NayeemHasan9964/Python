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

#Function to mutiply each number in a list with 2
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

#Function to replace the an item in a list with a new item,if the item is found in the list
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
def largest_swap(num):
        R_num = 0
        while num > 0:
                num1 = num % 10
                R_num = R_num*10 +  num1
                num = num // 10
        if (R_num > num):
                return R_num
        else:
                return num   
print(largest_swap(27))
