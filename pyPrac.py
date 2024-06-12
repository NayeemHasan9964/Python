print('Welcome to Python Programming')
# name=input("name:")
# a=int(input("a="))
# b=int(input("b="))
# sum=a+b
# print("Sum =",sum)

## List 
list=[1,2,45,56,"Me"] #Syntax of list
print(list[0])
list.append(4)
print(list)
#There are lot other Methods check notes or python Docs for more

## List-->Question WPA to enter the three movies of me in the list
print("Question Based on List \n")
Movies=[  ]
mov1=input("mov1:")
mov2=input("mov2:")
mov3=input("mov3:")
Movies.append(mov1)
Movies.append(mov2)
Movies.append(mov3)
print(Movies)

## Q2-->Check whether the given list has palindrome elements or not

Org_list=[1,3,2,1]

Copy_List=Org_list.copy()
Copy_List.reverse()

if(Copy_List == Org_list):
    print("Palindrome")
else:
    print("Not a palindrome")

## Tuple

tuple=(1,3,5,6)
print(tuple)


