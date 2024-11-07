# # 1. Basic String Manipulation
# # Write a function to reverse a string without using built-in functions.
# def rev_String(s):
#     reversed_string = ""
#     for char in s.lower():
#         reversed_string = char + reversed_string
#     return  reversed_string
# print(rev_String("Hello"))
#
#
# # Write a function to check if a string is a palindrome.
# def String_palindrome(s):
#     s = s.lower()
#     reversed_string = ""
#     for char in s:
#         reversed_string = char + reversed_string
#     print(reversed_string)
#     if reversed_string == s:
#         return "palindrome"
#     else:
#         return "not a Palindrome"
# print(String_palindrome("MADAM"))
#
# # Write a function to count vowels and consonants in a string.
# def countingVowelsAndConsonants(word):
#     vowels = "aeiouAEIOU"
#     c_count,v_count = 0,0
#     for char in word:
#         if char.isalpha():
#             if char in vowels:
#                 v_count += 1
#             else:
#                 c_count +=1
#     return c_count,v_count
# print(countingVowelsAndConsonants("hello"))
#
# # 2. Prime Numbers and Number Manipulations
#
# # Write a function to check if a given number is prime.
# def to_checkPrime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#         else:
#             return f"{num} is a prime"
# print(to_checkPrime(5))
# # Write a function to print all prime numbers within a range.
# def to_PrimeInRange():
#     lower = 2
#     upper = 100
#     print("Prime numbers between", lower, "and", upper, "are:")
#     for num in range(lower, upper + 1):
#         # all prime numbers are greater than 1
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 print(num)
# to_PrimeInRange()
# Write a function to find the sum of digits of a given number.
def sumOfDigits(num):
    sum = 0
    while num > 0:
        sum = sum + num%10
        num = num//10
    return sum
print(sumOfDigits(420))


