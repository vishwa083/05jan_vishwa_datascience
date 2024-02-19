#Write a Python program to test whether a passed letter is a vowel or not
letter = input("Enter a letter: ")

vowels = ['a', 'e', 'i', 'o', 'u']

if letter.lower() in vowels:
    print(letter, "is a vowel.")
else:
    print(letter, "is not a vowel.")