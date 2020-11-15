# Homework 2

# Prepared by Maksym Bilyi, id: 101169

# Step 1: importing a Shakespeare's poem in txt format
# + already applying lower function
poem = open("/Users/macbook/Desktop/Shakespeare.txt").read().lower()
print(poem)

# Step 2: importing neccessary libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from collections import Counter

# Step 3: tokenizing words and removing stop words
# every words is being treated as a separete token
# stop words (e.g. "the") are being removed
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(poem)
filtered = [w for w in tokens if not w in stop_words]
filtered = []
for w in tokens:
    if w not in stop_words:
        filtered.append(w)

# Step 4: removing special characters
filtered_2 = [character for character in filtered if character.isalnum()]

# Step 5: counting word frequencies
counts = Counter(filtered_2)
print(counts)