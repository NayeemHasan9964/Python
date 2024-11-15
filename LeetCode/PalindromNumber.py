def isPalindrome(x: int) -> bool:
    rev = 0
    Original_num = x
    while x > 0:
        rev = rev * 10 + x % 10
        x = x // 10
    print(rev)
    if Original_num== rev:
        return True
    else:
        return False
print(isPalindrome(121))