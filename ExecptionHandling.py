#Exception Handling
print("Learning Exception Handling")
num = 2
# if num % 0 == 0:
#     print("Even Number")
try:
    if num%0==0:
        print("Even Number")

except Exception as e:
    print(e)

finally:
    print("Final block is getting Executed")