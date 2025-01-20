elements = input("Enter elements: ").split()
my_tuple = tuple(elements)
for i in range(len(my_tuple)):
    print(f"Value {i + 1}: {my_tuple[i]}")
