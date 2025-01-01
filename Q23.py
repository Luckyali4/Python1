# Q23.Write a python program finding the factorial of a given number using a while loop?
def factorial(num):
    result = 1
    while num > 0:
        result *= num  
        num -= 1  
    return result
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}.")
