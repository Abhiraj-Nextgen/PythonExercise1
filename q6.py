a = 0
b = 1
while b <= 50:
    print(b, end=" ")
    temp = b
    b = a + b
    a = temp
