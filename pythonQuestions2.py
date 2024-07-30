#Function to calculate the BMI of a person
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi ,2)
print(calculate_bmi(78.2,6.2))

#Function to Reverse a number
def reverse_number(num):
    rev_num =  int(str(num)[::-1])
    if(rev_num > num):
        return False
    else:
        return True
print(reverse_number(27))    
