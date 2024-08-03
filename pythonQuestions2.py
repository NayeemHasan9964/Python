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
def multiply_by_two(numbers):
    multiplied_list = []
    for num in numbers:
        multiplied_list.append(num * 2)
    return multiplied_list
print("The multiplied list is:" ,multiply_by_two([1, 2, 3, 4, 5]))
       