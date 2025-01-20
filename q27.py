num_tuples = int(input("Enter the number of tuples: "))
tuples_list = []
for i in range(num_tuples):
    elements = input("Enter tuple elements: ").split()
    current_tuple = []
    for item in elements:
        current_tuple.append(int(item))
    tuples_list.append(tuple(current_tuple))
result = [0] * len(tuples_list[0])

for t in tuples_list:
    for i in range(len(t)):
        result[i] += t[i]
print("Element-wise sum of the said tuples:", tuple(result))