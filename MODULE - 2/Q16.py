#Write a Python program to count the occurrences of each word in a given sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print("Occurrences of each word in the sentence:")
for word, count in word_counts.items():
    print(f"'{word}': {count}")