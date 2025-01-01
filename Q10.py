#Q10.Write a program to convert Kilometers to Miles ?
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor
conversion_factor = 0.621371
# Convert kilometers to miles
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
