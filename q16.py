num = input("Enter a number: ")
reversed_num = ""
for digit in num:
    reversed_num = digit + reversed_num
if num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")