word = input("Enter a word: ").lower()
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
