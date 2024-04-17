a = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element: "))
    a.append(element)

largest = a[0]
for num in a:
    if num > largest:
        largest = num

print("Largest number in the list:", largest)
