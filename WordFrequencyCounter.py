from collections import Counter

text = input("Enter text: ").lower()
words = text.split()
counter = Counter(words)

print("📊 Word frequencies:")
for word, count in counter.items():
    print(f"{word}: {count}")
