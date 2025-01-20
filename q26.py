elements = input("Enter tuple elements: ").split()
my_tuple = tuple(elements)
item = input("Enter the item to find its index: ")
if item in my_tuple:
    index = my_tuple.index(item)
    print(f"The index of '{item}' is:", index)
else:
    print(f"'{item}' is not in the tuple.")
