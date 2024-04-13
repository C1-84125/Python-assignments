# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Main program
choice = input("Enter '1' to convert Celsius to Fahrenheit, or '2' to convert Fahrenheit to Celsius: ")

if choice == '1':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("The temperature in Fahrenheit is:", fahrenheit)
elif choice == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("The temperature in Celsius is:", celsius)
else:
    print("Invalid choice!")