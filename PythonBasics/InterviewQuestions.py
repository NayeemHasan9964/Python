# 1. Basic String Manipulation

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
#     rev = 0
#     while num>0:
#         n = num%10
#         rev = rev*10 + n
#         num = num//10
#     return rev
# print(rev_num(1234))

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
#     return max_num,min_num
# print(max_min_numInList([13,23,11,45,38,68]))
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
#
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
def anagrams(s1,s2):
    return sorted(s1)==sorted(s2)
print(anagrams("listen","hello"))

# 6. Finding the Greatest Common Divisor (GCD)
# Write a function to find the GCD of two numbers.
