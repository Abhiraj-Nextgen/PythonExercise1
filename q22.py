letter = input("Enter a letter: ").lower()
if len(letter) == 1 and letter.isalpha():
    vowels = "aeiou"
    if letter in vowels:
        print(letter, "is a vowel.")
    else:
        print(letter, "is a consonant.")

