from nltk.stem import PorterStemmer, LancasterStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
words = ['use', 'used', 'using', 'user', 'usable', 'usability', 'university', 'universe']

for w in words:
    print(w, porter.stem(w), lancaster.stem(w))
