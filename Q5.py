#Q5. write a program for assignment operators
num = int(input("Enter an initial number: "))
print(f"Initial value: {num}")
num += 5  
print(f"After 'num += 5': {num}")
num -= 3  
print(f"After 'num -= 3': {num}")
num *= 2
print(f"After 'num *= 2': {num}")
num /= 4  
print(f"After 'num /= 4': {num}")
num //= 2  
print(f"After 'num //= 2': {num}")
num %= 3  
print(f"After 'num %= 3': {num}")

num **= 2  
print(f"After 'num **= 2': {num}")
