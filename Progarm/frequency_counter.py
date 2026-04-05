from collections import Counter
import re

text = """Python is powerful. Python is easy to learn. 
Many developers love Python because it is versatile."""

# Clean text
words = re.findall(r'\w+', text.lower())
counter = Counter(words)

print("Top 5 words:", counter.most_common(5))
