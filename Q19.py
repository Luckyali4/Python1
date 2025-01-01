# Q19.Using max() and min() functions display the maximum and minimum of 5 random numbers?
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
maximum = max(random_numbers)
minimum = min(random_numbers)
print("Random numbers:", random_numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)
