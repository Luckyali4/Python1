#Q7.Write a program to calculate greatest of three numbers?
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print(f"The greatest number is: {a}")
elif b > c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")
