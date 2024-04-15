#This code was done by Shubham Mhaske
def calculate_compound_interest(principal, rate, time):
    """This function calculates compound interest."""
    amount = principal * ((1 + rate / 100) ** time)
    interest = amount - principal
    return interest

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period in years: "))

# Calculating compound interest using the function
compound_interest = calculate_compound_interest(principal, rate, time)
print(f"The compound interest is: {compound_interest}")
