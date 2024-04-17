#This code was drafted by Shubham Mhaske 84125
for num in range(11):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
