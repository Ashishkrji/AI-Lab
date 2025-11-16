#Predict the category to which a given piece of text belongs.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


texts = ["I love football", "This team scored a goal",
         "Python is great", "I write code in Python"]
lables = ["sports", "sports", "tech", "tech"]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)


model = MultinomialNB()
model.fit(X, lables)

test = ["I enjoy coding in Python"]
X_test = vectorizer.transform(test)
print("Predicted Category:", model.predict(X_test)[0])