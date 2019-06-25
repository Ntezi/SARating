from __future__ import unicode_literals, print_function
from spacy.lang.en import English  # updated

import pickle
import pandas as pd
from preprocess import Preprocess, GetFile
from test import Test, ModelFiles

from boto_nlp import BotoNLP

model_file = ModelFiles().naive_model_file


class TestHotelAspects:
    def __init__(self, test_data_file, ):
        encoding = 'latin-1'

        test_data = Preprocess().get_ready_data(test_data_file, encoding)

        self.tester(test_data)

    def tester(self, test_data):
        x_test = test_data['sentences']
        y = 'aspects'

        results_file = GetFile().hotel_aspects_result_file

        Test(y, test_data, x_test, model_file, results_file)


class ClassifyHotelAspects:
    def __init__(self, test_data_file):
        encoding = 'latin-1'
        sample = 5

        # test_data = Preprocess().get_sample_data(test_data_file, sample, encoding)
        test_data = Preprocess().get_ready_data(test_data_file, encoding)
        self.get_aspects(test_data)

        # aspects_with_sentiment_aws_file = GetFile().aspects_with_sentiment_aws_file
        # self.merge_aspects_and_sentiments_with_reviews(aspects_with_sentiment_aws_file)

    def classify_aspects(self, test_data):
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('sentencizer'))

        aspects = []
        for index, row in test_data.iterrows():
            doc = nlp(str(row['review']))

            model = pickle.load(open(model_file, 'rb'))

            for sent in doc.sents:
                x_test = [sent.text]
                y_test = model.predict(x_test)
                x_test = ', '.join(x_test)
                y_test = ', '.join(y_test)
                aspect = (index, x_test, y_test)
                aspects.append(aspect)
        return aspects

    def get_aspect_num(self, pd, name):
        aspect_num = []
        for index, row in pd.iterrows():
            num = row['aspects'].count(name)
            aspect_num.append(num)
        return aspect_num

    def get_aspects(self, test_data):

        test_data['index'] = test_data.index

        # Save sentences with  their aspects
        aspects = self.classify_aspects(test_data)
        df_aspects = pd.DataFrame(aspects, columns=['index', 'sentences', 'aspects'])

        # merge aspects with reviews
        self.merge_aspects_with_reviews(test_data, df_aspects)

        aspects_file = GetFile().aspects_file
        df_aspects.to_csv(aspects_file)

        # Sentiments analysis with aws boto at sentence level
        # BotoNLP(aspects_file)

    def merge_aspects_with_reviews(self, test_data, df_aspects):

        grouped_aspects = df_aspects.groupby('index')['aspects'].apply(lambda x: ';'.join(x.astype(str))).reset_index()
        merged_aspects_with_reviews = pd.merge(test_data, grouped_aspects[['index', 'aspects']], on='index')

        merged_aspects_with_reviews['aspects'] = merged_aspects_with_reviews['aspects'].str.split(';')

        merged_aspects_with_reviews['breakfast_food_drink'] = self.get_aspect_num(merged_aspects_with_reviews,
                                                                                  'breakfast & food & drink')
        merged_aspects_with_reviews['comfort_facilities'] = self.get_aspect_num(merged_aspects_with_reviews,
                                                                                'comfort & facilities')
        merged_aspects_with_reviews['location'] = self.get_aspect_num(merged_aspects_with_reviews, 'location')
        merged_aspects_with_reviews['miscellaneous'] = self.get_aspect_num(merged_aspects_with_reviews, 'miscellaneous')
        merged_aspects_with_reviews['overall'] = self.get_aspect_num(merged_aspects_with_reviews, 'overall')
        merged_aspects_with_reviews['service_staff'] = self.get_aspect_num(merged_aspects_with_reviews,
                                                                           'service & staff')
        merged_aspects_with_reviews['value_for_money'] = self.get_aspect_num(merged_aspects_with_reviews,
                                                                             'value for money')

        result_merged_with_aspects_file = GetFile().tripadvisor_hotel_reviews_result_merged_with_aspects_file
        merged_aspects_with_reviews.to_csv(result_merged_with_aspects_file)


    def merge_aspects_and_sentiments_with_reviews(self, aspects_with_sentiment_aws_file):

        encoding = 'latin-1'

        df_aspects_sentiments = Preprocess().get_data(aspects_with_sentiment_aws_file, encoding)

        x = df_aspects_sentiments.groupby(['aspects', 'sentiments']).size().unstack(fill_value=0)

        x.stack()
        a = x.to_dict('index')

        print(a)


if __name__ == '__main__':
    hotel_aspects_test_file = GetFile().hotel_aspects_test_file
    # TestHotelAspects(hotel_aspects_test_file)

    tripadvisor_hotel_reviews_result_file = GetFile().tripadvisor_hotel_reviews_result_file
    ClassifyHotelAspects(tripadvisor_hotel_reviews_result_file)
