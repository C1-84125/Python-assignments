#This code was done by Shubham Mhaske

def calculate_cube(num):
    """This function calculates the cube of a given number."""
    return num * num * num

# Taking 5 integer input values
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(5)]

# Calculating sum of cubes of all numbers
sum_of_cubes = sum([calculate_cube(num) for num in numbers])
print(f"The sum of the cubes of the numbers is: {sum_of_cubes}")
