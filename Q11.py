#Q11.Find the simple interest on RS.200  for 5 years at 5% per year?
principal = int(input("enter principles"))
rate = int(input("enter rate"))     
time =int(input("enter time"))      
# Calculate simple interest
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% per year is Rs. {simple_interest:.2f}.")
