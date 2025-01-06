# Retrieve last n numbers from a List
# def retrieve_last_elements(lst,n):
#     if n<=0:
#         return []
#     return lst[-n:]
# print(retrieve_last_elements([1,2,3,4,5],2))

# Check if given String is in the middle of the other string
# def is_in_center(s1, s2):
#     middleChar = s2[len(s2)//2]
#     if middleChar==s1[0]:
#         return True
#     else:
#         return False
# print(is_in_center('abc','xxabcxx')

# Excuse Threes
# def excuse_threes(n):
#     lst = []
#     for i in range(0,n+1):
#         if i%3==0:
#             continue
#         else:
#             lst.append(i)
#     return lst
# print(excuse_threes(10))

# Max_Score Divisibility
# def max_divisibility_score(n):
#     if n <= 0:
#         return None
#
#     scores = []
#
#     def find_div_score(num):
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         return count
#
#     for num in range(1, n + 1):
#         scores.append(find_div_score(num))
#     print(scores)
#     max_score = max(scores)
#     return scores.index(max_score) + 1
# print(max_divisibility_score(10))

# Prime Factors of a Number
# def prime_factors(n):
#     prime_factors_set = set()
#     divisor = 2
#
#     while n > 1:
#         while n % divisor == 0:
#             prime_factors_set.add(divisor)
#             n //= divisor  # Reduce n
#
#         divisor += 1
#
#     return list(prime_factors_set)
#
# print(prime_factors(56))

# Circular Shift
# def circular_shift(lst):
#     circularLst = [lst[-1]]
#     for i in range(0,len(lst)-1):
#         circularLst.append(lst[i])
#     return circularLst
# print(circular_shift([1,2,3,4,5]))

# Similar items in a list to dictionary
# def group_items(lst):
#     groups = {}
#     for index, item in enumerate(lst):
#         if item not in groups:
#             groups[item] = []
#         groups[item].append(index)
#     return groups
# print(group_items(['apple','banana','apple','banana']))

# Correct a Sentence
# def correct_sentence(sentence):
#     sentence = sentence.strip().capitalize()
#     if sentence[-1] != '.':
#         sentence += '.'
#
#     return f"{sentence.strip()}"
#
# print(correct_sentence('this is a test'))