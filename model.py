import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from nltk.corpus import stopwords

# Load and preprocess the dataset
df = pd.read_csv('Dataset/spam2.csv', encoding='utf-8')
df.dropna(how="any", inplace=True, axis=1)
df.columns = ['label', 'text']
df['label_num'] = df.label.map({'ham':0, 'spam':1})
df['message_len'] = df.text.apply(len)

def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    STOPWORDS = stopwords.words('english')
    #punctuation checking
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    # Removing Stopwords
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS])

df['clean_msg'] = df.text.apply(text_process)
X = df.clean_msg
y = df.label_num
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)
nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)

def getLabel(text):
    custom_text = text
    custom_text_dtm = vect.transform([custom_text])
    prediction = nb.predict(custom_text_dtm)
    label2num = ["ham", "spam"]
    predicted_label = label2num[prediction[0]]
    return predicted_label

print(getLabel("credit card payment of 2000"))
print(getLabel("what are you doing?"))
