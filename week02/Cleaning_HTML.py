#!/usr/bin/env python3
"""
Fetch and clean the full Wikipedia article HTML.
Extracts readable text only (paragraphs, lists).
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re

URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"
OUTFILE = Path("ai_article_clean.txt")
HEADERS = {
    "User-Agent": "script:ai-html-cleaner:1.0 (contact: example@example.com)"
}

def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.text

def extract_clean_text(html_source: str) -> str:
    soup = BeautifulSoup(html_source, "html.parser")

    # remove unwanted sections
    for tag in soup([
        "script", "style", "noscript", "table", "sup", "span",
        "figure", "img", "nav", "header", "footer"
    ]):
        tag.decompose()

    # get main content
    main = soup.find("div", id="mw-content-text")
    if not main:
        main = soup

    # collect all readable text
    texts = []
    for el in main.find_all(["p", "li"], recursive=True):
        t = el.get_text(" ", strip=True)
        if len(t.split()) > 3:
            texts.append(t)

    text = "\n\n".join(texts)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def main():
    html = fetch_html(URL)
    clean_text = extract_clean_text(html)

    OUTFILE.write_text(clean_text, encoding="utf-8")
    print("Saved full cleaned article text to:", OUTFILE)
    print("\n--- Full Article Text ---\n")
    print(clean_text)

if __name__ == "__main__":
    main()
