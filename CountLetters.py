from collections import Counter
input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "").lower()
letter_count = Counter(input_string)
print("\nHistogram of letter frequencies:")
for letter, count in letter_count.items():
    print(f"{letter}: {'*' * count}")
