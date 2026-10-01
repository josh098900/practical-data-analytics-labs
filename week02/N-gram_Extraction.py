from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords #added for stopwords 
nltk.download('stopwords', quiet=True)
import re
from nltk.stem import PorterStemmer

# Load text file
with open('ai_article_clean.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower() # tbis makes everything lower case 

# Simple tokenization (split on non-word characters)
tokens = re.findall(r'\b\w+\b', text) #regex, \w+ means one or more letters, digits or underscores, and \b marks a word boundary, this pulls out every word and drops punctuation
#removing stopwords 
stop = set(stopwords.words('english')) #this loads the list of stopwords from nltk, set() stores list as srt, as searching is word in set is faster than searching list
tokens = [t for t in tokens if t not in stop] #keep each token t only if its not in stop
tokens = [t for t in tokens if len(t) > 1] #keep each token t only if its longer than 1 character, this drops single letters like e and g in e.g which was coming up
porter = PorterStemmer() #this creates a stemmer object, which can be used to stem words
tokens = [porter.stem(t) for t in tokens]



# Generate n-grams
unigrams = Counter(tokens) 
bigrams = Counter(ngrams(tokens, 2)) # ngrams(tokens, 2) slides a window of size 2 along the token list, producing pairs
trigrams = Counter(ngrams(tokens, 3)) #counter is a dictionary that counts things eg, {the: 900, ai: 300, ...}

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


#print top 10 of each
print("Top unigrams:", unigrams.most_common(10))
print("Top bigrams:", bigrams.most_common(10))
print("Top trigrams:", trigrams.most_common(10))