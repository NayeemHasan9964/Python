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

#Total time spend on Washing Hands
# def total_washing_time(times_per_day, months):
#     oneHandWashInSeconds = 21
#     totalSecondsInADay = oneHandWashInSeconds * times_per_day
#     convertingIntoMinutes = totalSecondsInADay/60
#     totalTimeInMonths = (convertingIntoMinutes * 30) * months
#     totalMinutes = int(totalTimeInMonths)
#     totalSeconds = round((totalTimeInMonths - totalMinutes) * 60)
#     return f"{totalMinutes} minutes and {totalSeconds} seconds"
# print(total_washing_time(5,3))

# Check value is in Dict or not
# def value_exist(dict1, val):
#     for values in dict1:
#         if dict1[values]==val:
#             return True
#     return False
# print(value_exist({'a':1,'b':2},1))

# Triple Function
# def triple_function(a,b,c):
#     if a == True and b == True and c == True:
#         return True
#     else:
#         return False
# print(triple_function(True,False,True))

# String can be obtained from another string
# def is_long_pressed(name, typed):
#     name_list = list(name)
#     name_typed = list(typed)
#     for i in range(0, len(typed)):
#         if name_list[i] == name_typed[i]:
#             continue
#         else:
#             name_list.insert(i,name_typed[i])
#     return name_list==name_typed
# print(is_long_pressed("alex","aaleex"))

# Pronounce of X,s
# def pronounce_xs(s):
#     vowels = 'aeiouAEIOU'
#     result = []
#     i = 0
#
#     while i < len(s):
#         if s[i] == 'x':
#             if i + 1 < len(s) and s[i + 1] in vowels:
#                 result.append("cks")
#             else:
#                 result.append("k")
#         else:
#             result.append(s[i])
#         i += 1
#
#     return ''.join(result)
# print(pronounce_xs("xerox"))

# convert a color from CMYK format to RGB format
# def cmyk_to_rgb(cmyk):
#     c,m,y,k =  cmyk
#     R = 255 * (1-c)*(1-k)
#     G = 255 * (1-m)*(1-k)
#     B = 255 * (1-y)*(1-k)
#     return round(R),round(G),round(B)
# print(cmyk_to_rgb([0.4,0.49,0.552,0.36]))

# heterogeneous Dict
def filter_dict(d):
    result = {key: value for key, value in d.items() if isinstance(value, int)}
    return result
print(filter_dict({'a':1,'b':'2','c':3.0,'d':[4],'e':5}))



