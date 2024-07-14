# import libraries
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk


def tokenize(data, column_name):
    tokenized = [word_tokenize(entry) for entry in data[column_name].to_list()]

    return tokenized

# remove stopwords and non-words (e.g., numbers)
def preprocess(sentence, filter=False):
    if filter == True:
        stopwords = nltk.corpus.stopwords.words('english')
        filtered_text = [token.lower() for token in sentence if token.lower() not in stopwords and token.isalpha()]
        return filtered_text
    else:
        preprocessed = [token.lower() for token in sentence]
        return preprocessed


# create bag of words model
# function to create a dict with 0 count for every word
def create_dict(tokenized_docs):
    vocabs = {}
    
    for document in tokenized_docs:
        for token in document:
            if token.lower() not in vocabs.keys():
                vocabs[token.lower()] = 0
            else:
                pass
    
    return vocabs
