# def is_pronic(n):
#     for i in range(1,n+1):
#         if i*(i+1)==n:
#             print(i*(i+1))
#             return True
#     return False
# print(is_pronic(6))

# def can_type(keys, word):
#     keys = sorted(keys)
#     word = sorted(word)
#     return keys == word
# print(can_type('abc','bac'))

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



