#This code was drafted by Shubham Mhaske 84125
for a in range(12):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    print(f"The factorial of {a} is {factorial}")
