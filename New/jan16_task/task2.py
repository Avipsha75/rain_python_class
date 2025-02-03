from collections import Counter
paragraph ="""
The rain fell steadily, and the sound of rain filled the air. The rain tapped softly on the windows, creating a rhythmic melody that seemed to echo through the room. Outside, the rain washed the streets clean, leaving a glistening sheen on every surface. The rain brought with it a sense of calm, a sense of quiet, as if the world itself was taking a breath. It was a moment when the rain connected everything, a gentle reminder of its power and its presence.
"""

words = paragraph.lower().split()
word_counts = Counter(words)

top_repeated = word_counts.most_common(3)

print("Word Count: ")
for word, count in top_repeated:
    print(f"{word}: {count}")
 
