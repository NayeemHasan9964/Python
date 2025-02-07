# 1. Basic String Manipulation
from PIL.GimpGradientFile import linear


# Write a function to reverse a string without using built-in functions.
# def rev_String(s):
#     reversed_string = ""
#     for char in s.lower():
#         reversed_string = char + reversed_string
#     return  reversed_string
# print(rev_String("Hello"))

# Write a function to check if a string is a palindrome.
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

# Write a function to count vowels and consonants in a string.
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


#2. Prime Numbers and Number Manipulations
# Write a function to check if a given number is prime.
# def to_checkPrime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#         else:
#             return f"{num} is a prime"
# print(to_checkPrime(5))

# Write a function to print all prime numbers within a range.
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
# def sumOfDigits(num):
#     sum = 0
#     while num > 0:
#         sum = sum + num%10
#         num = num//10
#     return sum
# print(sumOfDigits(420))

# Write a function to Reverse a number
# def rev_num(num):
#     x = num
#     rev = 0
#     while num>0:
#         n = num%10
#         rev = rev*10 + n
#         num = num//10
#     if rev == x:
#         return "Palindrome"
#     else:
#         return "not a Palindrome"
# print(rev_num(121))

# Write a function for fibonacci Series
# def fibonacci_series(n):
#     seq = [0,1]
#     while seq[-1]+seq[-2]<n:
#         seq.append(seq[-1]+seq[-2])
#     return seq
# print(fibonacci_series(25))

# 3. Working with Lists
# Write a function to find the second-largest element in a list.
# def to_findSecondLargest(lst):
#     max_num = lst[0]
#     for i in range(0, len(lst)):
#         if lst[i] > max_num:
#             max_num = lst[i]
#     lst.remove(max_num)
#     new_lst = lst
#     second_largest = new_lst[0]
#     for j in range(0, len(new_lst)):
#         if new_lst[j] > second_largest:
#             second_largest = new_lst[j]
#     return second_largest
# print(to_findSecondLargest([13,23,11,45,38,68]))


# Write a function to find the maximum and minimum in a list without using built-in functions.
# def max_min_numInList(lst):
#     max_num = lst[0]
#     min_num = lst[0]
#     for i in range(0,len(lst)):
#         if lst[i]>max_num:
#             max_num = lst[i]
#         elif lst[i]<min_num:
#             min_num = lst[i]
#     return min_num,max_num
# print(max_min_numInList([100,180,240,310,40,535,695]))
# Write a function to remove duplicates from a list.
# def to_removeDuplicates(lst):
#     i = 0
#     while i < len(lst):
#         j = i + 1
#         while j < len(lst):
#             if lst[i] == lst[j]:
#                 del lst[j]  # Remove the duplicate element at index j
#             else:
#                 j += 1  # Move to the next element only if no deletion occurred
#         i += 1  # Move to the next element in the outer loop
#     return lst
# print(to_removeDuplicates([13,23,11,45,38,11,68]))  # Output should be [1, 2, 3, 4, 5]


# Write a function to sort a list in descending order without using built-in sort functions
# def to_sortInDescending(lst):
#     for i in range(0,len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i]<lst[j]:
#                 lst[i],lst[j]=lst[j],lst[i]
#     return lst
# print(to_sortInDescending([11,88,77,66,55,44,33,22,99]))

# def to_sortInAscending(lst):
#     for i in range(0,len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i]>lst[j]:
#                 lst[i],lst[j]=lst[j],lst[i]
#     return lst
# print(to_sortInAscending([11,88,77,66,55,44,33,22,99]))

# 4. Recursion and Mathematical Operations
# Write a recursive function to find the factorial of a number.
# def factorial(n):
#     if n == 0:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive call
# print(factorial(3))

# 5. Finding Anagrams
# Write a function to check if two words are anagram
# def anagrams(s1,s2):
#     return sorted(s1)==sorted(s2)
# print(anagrams("listen","hello"))

# 6. Finding the Greatest Common Divisor (GCD)
# Write a function to find the GCD of two numbers.
# def GCD(a,b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(GCD(18,12))

# 7. String and List Comparison
# Write a function to find the longest word in a sentence and return its length.
# def longest_word(words):
#     max_length = len(words[0])
#     for i in range(0,len(words)):
#         if len(words[i])>max_length:
#             max_length = len(words[i])
#     return max_length
# print(longest_word(["Apple","Date","CherryPick"]))

# Write a function to merge two sorted lists into a single sorted list without using the sort function.
# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1
#     merged_list.extend(list1[i:])
#     merged_list.extend(list2[j:])
#     return merged_list
# print(merge_sorted_lists([1,3,5],[2,4,6]))

# 9. File Handling
# Write a Python program to read a file line by line and print each line.
# with open("practice.txt","r") as r:
#     for line in r:
#         print(line.strip())

# Write a function to count the number of lines and words in a file.
# line_count =0
# word_count=0
# with open("practice.txt","r") as counter:
#     for line in counter:
#         line_count+=1
#         words = line.split()
#         word_count +=len(words)
# print(line_count,word_count)

# Write a function using Try,except and Final Block
# def catch_exception(a,b):
#     try:
#         result = a//b
#         return  result
#     except Exception as e:
#         print(e)
#     finally:
#         print("Executed Successfully")
# print(catch_exception(10,0))

# Write a function for Perfect Number
# def perfect_Number(num):
#     divisors= []
#     if num <= 1:
#         return False
#     for i in range(1,num):
#         if num % i == 0:
#             divisors.append(i)
#     print(divisors)
#     if sum(divisors)== num:
#         return "PerfectNumber"
#     else:
#         return "Not a PerfectNumber"
# print(perfect_Number(496))

# class primeNumber:
#     @staticmethod
#     def primeOrNot(n):
#         for i in  range(2,n):
#             if n%i==0:
#                 break
#             else:
#                 return n
# obj = primeNumber()
# print(obj.primeOrNot(5))

# numbers are linear quadratic or cubic





