#This code was drafted by Shubham Mhaske 84125
def number_to_words(number):
    words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    result = ''
    for digit in str(number):
        result += words[digit] + ' '
    return result.strip()

number = int(input("Enter a number: "))
print(number_to_words(number))
