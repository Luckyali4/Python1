#Q6.Write a program for bitwise operator?
a = int(input("enter a number"))
b = int(input("enter second number"))
print("Bitwise Operations on a = 4 and b = 2:")
# Bitwise AND
result_and = a & b
print(f"a & b = {result_and}")
# Bitwise OR
result_or = a | b
print(f"a | b = {result_or}")  

# Bitwise XOR
result_xor = a ^ b
print(f"a ^ b = {result_xor}")  
# Bitwise NOT
result_not_a = ~a
print(f"~a = {result_not_a}")  
# Left Shift
result_left_shift = a << 1
print(f"a << 1 = {result_left_shift}")  
# Right Shift
result_right_shift = a >> 1
print(f"a >> 1 = {result_right_shift}") 
