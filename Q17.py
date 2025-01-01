# Q17. Declare a div() function with two parametrs.Then call the functiion and pass two numbers and display their division ?
def div(a1, a2):
    if a2 != 0:   
        return a1 / 2
    else:
        return "Division by zero is not allowed."
result = div (10, 2)
print("The result of the division is:", result)
