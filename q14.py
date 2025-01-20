numbers = input("Enter numbers: ").split()
array = []
for num in numbers:
    array.append(int(num))
largest = array[0]
for num in array:
    if num > largest:
        largest = num
print("Largest number using loop:", largest)
max_number = max(array)
print("Largest number using max() function:", max_number)