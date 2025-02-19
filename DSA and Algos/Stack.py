# Applications of Stack Data Structure
# Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:
# To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack,
# you will get the letters in reverse order.

# In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9)
# by converting the expression to prefix or postfix form.

# In browsers - The back button in a browser saves all the URLs you have visited previously in a stack.
# Each time you visit a new page, it is added on top of the stack. When you press the back button,
# the current URL is removed from the stack, and the previous URL is accessed.



# Write a function is_balanced(expression) that checks if the parentheses in a given expression are balanced.
# The function should return True if the expression is balanced and False otherwise.

def is_balanced(expression: str) -> bool:
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        if char == '(':
            stack.append(char)  # Push opening parenthesis to the stack
        elif char == ')':
            # If we encounter a closing parenthesis, check if the stack is empty
            if not stack:
                return False  # No matching opening parenthesis
            stack.pop()  # Pop the matching opening parenthesis
    print(stack)
    # If the stack is empty, parentheses are balanced
    return len(stack) == 0



# Test cases
print(is_balanced("((2+3) * (5+3))"))  # Output: True
print(is_balanced("((2+3) * (5+3))("))  # Output: False

