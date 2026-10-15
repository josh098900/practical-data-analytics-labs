import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# download resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# define paths
input_folder = "week03/Output"
output_unigram = "week03/Output/updated_result_1gram.csv"
output_bigram = "week03/Output/updated_result_2gram.csv"
output_trigram = "week03/Output/updated_result_3gram.csv"

# stop words
stop_words = set(stopwords.words('english'))

# load and clean text files
documents = []
doc_names = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        words = word_tokenize(text.lower())
        words = [w for w in words if w.isalpha() and w not in stop_words]
        documents.append(' '.join(words))
        doc_names.append(filename)

def process_ngrams(documents, doc_names, n, output_csv):
    # TF-IDF
    vectorizer = TfidfVectorizer(ngram_range=(n, n), max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out()

    # frequency counts
    term_frequencies = []
    for doc in documents:
        tokens = doc.split()
        ngrams = [' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
        counts = Counter(ngrams)
        term_frequencies.append(counts)

    # build table
    data = []
    for i, term in enumerate(terms):
        row = [term]
        total = 0
        for doc_counts in term_frequencies:
            freq = doc_counts.get(term, 0)
            row.append(freq)
            total += freq
        row.append(total)
        tfidf_score = tfidf_matrix.getcol(i).mean()
        row.append(round(tfidf_score, 4))
        data.append(row)

    columns = ["Term"] + doc_names + ["Total Frequency", "TFIDF Score"]
    df = pd.DataFrame(data, columns=columns)
    df = df.sort_values(by="Total Frequency", ascending=False).head(100)
    df.to_csv(output_csv, index=False)
    print(f"Top 100 {n}-grams saved to: {output_csv}")

# run for unigrams, bigrams, trigrams
process_ngrams(documents, doc_names, 1, output_unigram)
process_ngrams(documents, doc_names, 2, output_bigram)
process_ngrams(documents, doc_names, 3, output_trigram)
