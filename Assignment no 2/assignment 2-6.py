#This code was done by Shubham Mhaske
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3
grade = ''

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average <= 89:
    grade = 'B'
elif 70 <= average <= 79:
    grade = 'C'
elif 60 <= average <= 69:
    grade = 'D'
else:
    grade = 'F'

print(f"The average marks are {average} and the grade is {grade}.")
