import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
import re
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# input and output folders
input_folder = "week03/Clean_Texts"
output_folder = "week03/Output"

os.makedirs(output_folder, exist_ok=True)

stop_words = set(stopwords.words('english'))

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.lower()
            text = re.sub(r"[^a-z\s.]"," ", text)  # replace unwanted characters with a space, keeping full stops



        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        cleaned_text = ' '.join(filtered_words)

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

print("Cleaned files saved in:", output_folder)
