#This code was done by Shubham Mhaske
calls = int(input("Enter the number of calls: "))
total_cost = 0

if calls <= 100:
    total_cost = 200
elif calls <= 150:
    total_cost = 200 + (calls - 100) * 0.60
elif calls <= 200:
    total_cost = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    total_cost = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40

print(f"The total telephone bill is: Rs. {total_cost:.2f}")
