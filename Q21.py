# Q21.Write a python program to reverse a number using a while loop?
# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + remainder  # Build the reversed number
        num = num // 10  # Remove the last digit
    return reversed_num

# Input from the user
number = int(input("Enter a number to reverse: "))
reversed_number = reverse_number(number)

# Output the reversed number
print("Reversed Number:", reversed_number)
