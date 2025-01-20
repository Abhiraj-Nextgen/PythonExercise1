list1 = input("Enter elements of the first list: ").split()
list2 = input("Enter elements of the second list: ").split()
for item in list1:
    list2.append(item)
print("New list:", list2)
