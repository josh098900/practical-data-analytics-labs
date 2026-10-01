import re
text = "hello \n world"
print("---")
print(re.sub(r"\s{2,}", " ", text))
print("---")
print(re.sub(r"[ \t]{2,}", " ", text))


#"hello   world"
# ---
# hello world
# ---
# hello world



#"AI is a field.\n\nIt began in 1956."
# ---
# AI is a field. It began in 1956.
# ---
# AI is a field.

# It began in 1956.



# "hello\nworld"
# hello
# world
# ---
# hello
# world


#"hello \n world"
# ---
# hello world
# ---
# hello 
#  world