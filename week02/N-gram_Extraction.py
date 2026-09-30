from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import nltk
import re

# Load text file
with open('ai_article_clean.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Simple tokenization (split on non-word characters)
tokens = re.findall(r'\b\w+\b', text)

# Generate n-grams
unigrams = Counter(tokens)
bigrams = Counter(ngrams(tokens, 2))
trigrams = Counter(ngrams(tokens, 3))

# Save to files
with open('unigrams.txt', 'w', encoding='utf-8') as f:
    for k, v in unigrams.items():
        f.write(f"{k}\t{v}\n")

with open('bigrams.txt', 'w', encoding='utf-8') as f:
    for k, v in bigrams.items():
        f.write(f"{' '.join(k)}\t{v}\n")

with open('trigrams.txt', 'w', encoding='utf-8') as f:
    for k, v in trigrams.items():
        f.write(f"{' '.join(k)}\t{v}\n")