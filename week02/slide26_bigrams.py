#what i want
#a dictionarry of page names and urls to loop over
#to reuse the cleaning functions i already fixed
#one bigram file per page, sorted by count
#one chart per page, saved as an image

#up2255832 feel free to use my work to understand how to do this, just dont copy and paste lol 
import re
import time
from collections import Counter
from pathlib import Path

import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams

from Cleaning_HTML import fetch_html, extract_clean_text

PAGES = {
    "algorithm": "https://en.wikipedia.org/wiki/Algorithm",
    "artificial_intelligence": "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "computer_architecture": "https://en.wikipedia.org/wiki/Computer_architecture",
    "cybersecurity": "https://en.wikipedia.org/wiki/Computer_security",
    "data_structure": "https://en.wikipedia.org/wiki/Data_structure",
    "machine_learning": "https://en.wikipedia.org/wiki/Machine_learning",
    "operating_system": "https://en.wikipedia.org/wiki/Operating_system",
    "programming_language": "https://en.wikipedia.org/wiki/Programming_language",
    "software_engineering": "https://en.wikipedia.org/wiki/Software_engineering",
}

OUT_DIR = Path("slide26_output")
OUT_DIR.mkdir(exist_ok=True)

nltk.download("stopwords", quiet=True)
STOP = set(stopwords.words("english"))


def get_bigrams(text):
    tokens = re.findall(r"\b\w+\b", text.lower())
    # TODO 1: remove stopwords
    tokens = [t for t in tokens if t not in STOP]
    # TODO 2: remove single-character tokens
    tokens = [t for t in tokens if len(t) > 1]
    # TODO 3: return a Counter of bigrams
    return Counter(ngrams(tokens, 2))


def save_bigrams(name, bigrams):
    path = OUT_DIR / f"{name}_bigrams.txt"
    with open(path, "w", encoding="utf-8") as f:
        
        # TODO 4: write every bigram and its count, most common first
        for pair, count in bigrams.most_common():
            f.write(f"{' '.join(pair)}\t{count}\n")



def main():
    for name, url in PAGES.items():
        print(f"Processing {name}...")
        html = fetch_html(url)
        text = extract_clean_text(html)
        bigrams = get_bigrams(text)
        save_bigrams(name, bigrams)
        time.sleep(1)


if __name__ == "__main__":
    main()