from collections import Counter

#Sample text
text = """
Python is an amazing programming language. Python is fun to learn and powerful to use.
"""

#Split text into words and count frequency
words = text.lower().split()
word_counts = Counter(words)

#Display word frequencies
print("Word Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
    print(len(text))