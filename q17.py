sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result_list = []
for i in range(len(sample_list)):
    if i not in (0, 4, 5):
        result_list.append(sample_list[i])
print("New list:", result_list)
