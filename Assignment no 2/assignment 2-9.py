#This code was done by Shubham Mhaske
def calculate_simple_interest(principal, rate, time):
   
    interest = (principal * rate * time) / 100
    return interest

# Taking input from the user
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual interest rate: "))
time_period = float(input("Enter the time period in years: "))

# Calculating simple interest using the function
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)
print(f"The simple interest is: {simple_interest}")

