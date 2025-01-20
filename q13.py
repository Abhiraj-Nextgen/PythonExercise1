numbers = input("Enter numbers: ").split()
array = []
for num in numbers:
    array.append(int(num))
total = 1
for num in array:
    total *= num
print("Product using loop:", total)