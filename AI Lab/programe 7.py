from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
docs = [
    "I love programming",
    "Programming in Python is fun",
    "I love Python"
]

# Create the CountVectorizer object
vectorizer = CountVectorizer()

# Fit the model and transform the documents into a Bag of Words representation
X = vectorizer.fit_transform(docs)

# Display the words extracted
print("Words:", vectorizer.get_feature_names_out())

# Display the Bag of Words matrix
print("Bag of Words:\n", X.toarray())
