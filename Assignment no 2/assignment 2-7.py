#This code was done by Shubham Mhaske
quantity = int(input("Enter the quantity: "))
unit_price = 5
total_price = quantity * unit_price

if quantity > 50:
    total_price *= 0.85  # 15% discount
elif quantity > 30:
    total_price *= 0.90  # 10% discount

print(f"The total price for {quantity} items is: Rs. {total_price:.2f}")
