ans = []
for number in range(100, 401):
    all_even = True
    for digit in str(number):
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        ans.append(number)
print(ans)
