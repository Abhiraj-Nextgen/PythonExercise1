elements = input("Enter tuple elements:").split()
my_tuple = tuple(elements)
new_item = input("Enter the item to add: ")
result = my_tuple + (new_item,)
print("New tuple:", result)
