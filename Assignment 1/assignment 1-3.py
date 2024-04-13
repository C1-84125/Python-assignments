def display_face_value(number):
    digits = [int(digit) for digit in str(number)]
    print("Face value of each decimal digit:")
    for digit in digits:
        print(digit, end=" ")

def display_place_value(number):
    print("\nPlace value of each decimal digit:")
    for i, digit in enumerate(str(number)):
        place_value = int(digit) * (10 ** (3 - i))
        print(place_value, end=" + " if i < 3 else "")

def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

number = int(input("Enter a 4-digit number: "))

display_face_value(number)

display_place_value(number)

reversed_number = reverse_number(number)
print(f"\nReversed number: {reversed_number}")