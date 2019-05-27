from __future__ import unicode_literals, print_function
from spacy.lang.en import English  # updated

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

from preprocess import Preprocess, GetFile
from classify import Classifier
from test import Test


class TestHotelAspects:
    def __init__(self, train_data_file, test_data_file, results_file):
        encoding = 'latin-1'

        train_data = Preprocess().get_ready_data(train_data_file, encoding, 'train')
        test_data = Preprocess().get_ready_data(test_data_file, encoding, 'test')

        self.tester(train_data, test_data, results_file)

    def tester(self, train_data, test_data, results_file):
        x_train = train_data['sentences']
        y_train = train_data['aspects']
        x_test = test_data['sentences']
        y = 'aspects'

        classifier = MultinomialNB()
        features = ('bow', CountVectorizer(analyzer=Preprocess().get_text_tokens))

        Test(y, test_data, classifier, features, x_train, y_train, x_test, results_file)


class ClassifyHotelAspects:
    def __init__(self, train_data_file, test_data_file, results_file):
        encoding = 'latin-1'

        sample = 1500
        train_data = Preprocess().get_sample_data(train_data_file, sample, encoding)
        # train_data = Preprocess().get_ready_data(train_data_file, encoding, 'train')

        sample = 10
        test_data = Preprocess().get_sample_data(test_data_file, sample, encoding)
        # test_data = Preprocess().get_ready_data(test_data_file, encoding, 'test')

        x_train = train_data['sentences']
        y_train = train_data['aspects']

        self.classify(x_train, y_train, test_data, results_file)

    def get_aspects(self, test_data, classifier, features, x_train, y_train):
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
        return aspects

    def classify(self, x_train, y_train, test_data, results_file):
        classifier = MultinomialNB()
        features = ('bow', CountVectorizer(analyzer=Preprocess().get_text_tokens))
        # results_file = '../data/collections/results_1.csv'

        test_data['index'] = test_data.index

        aspects = self.get_aspects(test_data, classifier, features, x_train, y_train)
        df_sentences = pd.DataFrame(aspects, columns=['index', 'aspects'])
        groupby = df_sentences.groupby('index')['aspects'].apply(lambda x: ';'.join(x.astype(str))).reset_index()

        # groupby['aspects'] = ', '.join(map(str, groupby['aspects']))
        # print(groupby)

        results = pd.merge(test_data, groupby[['index', 'aspects']], on='index')
        results.to_csv(results_file)


if __name__ == '__main__':
    hotel_aspects_train_file = GetFile().hotel_aspects_train_file
    hotel_aspects_test_file = GetFile().hotel_aspects_test_file
    hotel_aspects_result_file = GetFile().hotel_aspects_result_file
    TestHotelAspects(hotel_aspects_train_file, hotel_aspects_test_file, hotel_aspects_result_file)

    tripadvisor_hotel_reviews_result_with_aspects_file = GetFile().tripadvisor_hotel_reviews_result_with_aspects_file
    tripadvisor_hotel_reviews_result_file = GetFile().tripadvisor_hotel_reviews_result_file
    ClassifyHotelAspects(hotel_aspects_train_file, tripadvisor_hotel_reviews_result_file, tripadvisor_hotel_reviews_result_with_aspects_file)