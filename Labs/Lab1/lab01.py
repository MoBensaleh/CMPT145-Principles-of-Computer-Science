import re
from collections import Counter
with open('sample.txt') as f:
    text = f.read().lower()
words = re.findall(r'\w+', text)
print(Counter(words).most_common(5))