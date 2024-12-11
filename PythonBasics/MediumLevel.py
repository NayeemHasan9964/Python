# def is_pronic(n):
#     for i in range(1,n+1):
#         if i*(i+1)==n:
#             print(i*(i+1))
#             return True
#     return False
# print(is_pronic(6))

def can_type(keys, word):
    keys = sorted(keys)
    word = sorted(word)
    return keys == word
print(can_type('abc','bac'))

