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
def time_saved(distance, speed1, speed2):
    print(distance/speed1- distance/speed2)
    return round(distance/speed1- distance/speed2,2)
print(time_saved(200,60,80))   