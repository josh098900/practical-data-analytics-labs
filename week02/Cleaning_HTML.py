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
#request.get downloads the page just like browser
#headers sends a user agent, a name tag saying whos asking, wikapedia blocks requests without one to stop anonymous scrapers
#timeout = 15, means it gives up after 15 secinds unstead of hanging forever
#raise_for_status crashses with a clear error if download fails, eg 404 instead of silently carrying on with a error page
#r.text is raw html as one long string
def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.text

#cleanup function, beauitful soup tuens html string into a tree you can search. 
def extract_clean_text(html_source: str) -> str:
    soup = BeautifulSoup(html_source, "html.parser")

    # remove unwanted sections
    for tag in soup([
        "script", "style", "noscript", "table", "sup", "span",
        "figure", "img", "nav", "header", "footer"
    ]):
        tag.decompose()
        #decompose() deletes each of those elements completely, along with everything inside them, 
        #script and style hold code and css which arennt text
        # table holds infoboxes and data tables
        #sup holds the little citation markers like [12]
        #nav, header, footer hold menus and site chrome. 
    # get main content
    main = soup.find("div", id="mw-content-text") # this narrows search to the div where wiki puts the article body
    #skipping the sidebar
    if not main:
        main = soup

    # collect all readable text
    texts = []
    for el in main.find_all(["p", "li"], recursive=True): #this keeps only paragraphs and list items, p and li
        t = el.get_text(" ", strip=True) #get_text() strips the tags and returns plain text
        if len(t.split()) > 3: # keeps a peice only if it has more than 3 words, drops stuff like edit or see also
            texts.append(t) 

    text = "\n\n".join(texts) #joins all the peices with a blank line between them
    text = re.sub(r"[\t]{2,}", " ", text) # regex, search and replace patterns, \s{2,} means 2 or more white space characters in a row, [\t] means a space or tab made it no longer output in a single line
    text = re.sub(r"\n{3,}", "\n\n", text) #\n{3,} means 3 or more newline characters in a row, each gets replaced  with something tidier
    return text.strip()

# fetch clean and save results to ai_article_clean.txt 
def main():
    html = fetch_html(URL)
    clean_text = extract_clean_text(html)

    OUTFILE.write_text(clean_text, encoding="utf-8")
    print("Saved full cleaned article text to:", OUTFILE)
    print("\n--- Full Article Text ---\n")
    print(clean_text)

if __name__ == "__main__":
    main()
