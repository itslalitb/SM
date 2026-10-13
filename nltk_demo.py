import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = "This is a very useful cloud computing course."

tokens = word_tokenize(text)
stop_words = set(stopwords.words("english"))

filtered = [
    word for word in tokens
    if word.lower() not in stop_words
]

print("Tokens:", tokens)
print("After stop word removal:", filtered)
