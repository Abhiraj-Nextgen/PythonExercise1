numbers = input("Enter numbers: ").split()
array = []
for num in numbers:
    array.append(int(num))
smallest = float('inf')
second_smallest = float('inf')
for num in array:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
if second_smallest == float('inf'):
    print("There is no second smallest number.")
else:
    print("The second smallest number is:", second_smallest)