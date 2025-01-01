# Q22.Write a python program to check whether a number is palindrome or not? 
# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert the number to a string and check if it is the same when reversed
    return str(num) == str(num)[::-1]

# Input from the user
number = int(input("Enter a number to check if it is a palindrome: "))

# Check and print the result
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
