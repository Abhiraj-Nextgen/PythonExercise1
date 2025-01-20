numbers = input("Enter numbers: ").split()
array = []
for num in numbers:
    array.append(int(num))
total = 0
for num in array:
    total += num
print("Sum using loop:", total)
total_sum = sum(array)
print("Sum using sum() function:", total_sum)
