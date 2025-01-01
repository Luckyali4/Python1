#Q8.Using input()function take one number from the user and using ternary operatorscheck whether the number is even or odd?
number = int(input("Enter a number: "))
# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"
# Print the result
print(f"The number {number} is {result}.")
