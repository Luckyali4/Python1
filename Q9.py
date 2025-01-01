#Q9.Using input function take two number and then swap the number?
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Print the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
# Swap the numbers
num1, num2 = num2, num1
# Print the numbers after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}")
