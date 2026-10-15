import re

text = "Python123 is awesome456"

result = re.sub(r"[0-9]", "", text)

print(result)

# Regex	Meaning
# [0-9]	Any digit
# [a-z]	Any lowercase letter
# [A-Z]	Any uppercase letter
# [a-zA-Z]	Any English letter
# \s	Whitespace (spaces, newlines, tabs)
# \d	Any Unicode decimal digit
# [^...]	Match any character not in the brackets
# \.	A literal full stop
# The ^ inside square brackets is particularly important for your task.
# [a-z] means match lowercase letters.
# [^a-z] means match everything except lowercase letters.

# import re

# text = "Artificial Intelligence (AI) grew 200% in 2025! AMAZING."

# # TODO 2: Convert text to lowercase
# text = text.lower()

# # TODO 1: Use re.sub() to remove unwanted characters
# text = re.sub(r"[^a-z\s]", "", text)

# print(text)
#replace unwated characters with a space, keeping full stops
import re

text = "Machine-learning uses rule-based decision-making."

text = text.lower()

text = re.sub(r"[^a-z\s.]"," ", text)

print(text)

# machine learning uses rule based decision making age too red
# number of n grams = W - N +1