from __future__ import unicode_literals, print_function
from spacy.lang.en import English  # updated
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

from preprocess import Preprocess, GetFile
from classify import Classifier
from test import Test

encoding = 'latin-1'
sample = 500

train_data_file = GetFile().hotel_aspects_train_file
train_data = Preprocess().get_sample_data(train_data_file, sample, encoding)

sample = 2
test_data_file = GetFile().tripadvisor_hotel_reviews_result_file
test_data = Preprocess().get_sample_data(test_data_file, sample, encoding)

x_train = train_data['sentences']
y_train = train_data['aspects']
y = 'aspects'

classifier = MultinomialNB()
features = ('bow', CountVectorizer(analyzer=Preprocess().get_text_tokens))
results_file = '../data/collections/results_1.csv'


nlp = English()
nlp.add_pipe(nlp.create_pipe('sentencizer'))

aspects = []
for index, row in test_data.iterrows():
    doc = nlp(str(row['review']))
    for sent in doc.sents:
        x_test = [sent.text]
        y_test = Classifier().fit_test_classifier(classifier, features, x_train, y_train, x_test)
        y_test = ', '.join(y_test)
        aspect = (index, y_test)
        aspects.append(aspect)
test_data['index'] = test_data.index
df_sentences = pd.DataFrame(aspects, columns=['index', 'aspects'])
groupby = df_sentences.groupby('index')['aspects'].apply(lambda x: ';'.join(x.astype(str))).reset_index()

# groupby['aspects'] = ', '.join(map(str, groupby['aspects']))
# print(groupby)

results = pd.merge(test_data, groupby[['index', 'aspects']], on='index')
results.to_csv(results_file)


