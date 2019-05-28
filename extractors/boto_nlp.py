import boto3
import json
import pandas as pd
from preprocess import Preprocess, GetFile


class BotoNLP:
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    # data_file = GetFile().sentences_with_aspects_file

    # data = pd.read_csv(data_file, encoding="ISO-8859-1")

    # data = data.sample(n=10)

    def __init__(self, data_file):
        # language code
        language_code = 'en'

        # # detecting the dominant language
        # result = detect_dominant_language(text)
        # print("Starting detecting the dominant language")
        # print(json.dumps(result, sort_keys=True, indent=4))
        # print("End of detecting the dominant language\n")
        #
        # # detecting named entities
        # result = detect_entities(text, language_code)
        # print("Starting detecting named entities")
        # print(json.dumps(result, sort_keys=True, indent=4))
        # print("End of detecting named entities\n")
        #
        # # detecting key phrases
        # result = detect_key_phraes(text, language_code)
        # print("Starting detecting key phrases")
        # print(json.dumps(result, sort_keys=True, indent=4))
        # print("End of detecting key phrases\n")

        # detecting sentiment
        # result = detect_sentiment(text, language_code)
        # print(result['Sentiment'])

        encoding = 'ISO-8859-1'
        data = Preprocess().get_data(data_file, encoding)

        sentiments = []
        for index, row in data.iterrows():
            text = str(row['sentences'])
            result = self.detect_sentiment(text, language_code)
            # print(result['Sentiment'])
            y_test = result['Sentiment']
            sentiment = (index, y_test)
            sentiments.append(sentiment)

        df_sentiments = pd.DataFrame(sentiments, columns=['index', 'sentiments'])

        data['index'] = data.index
        merged_aspects_with_sentiments = pd.merge(data, df_sentiments[['index', 'sentiments']], on='index')
        merged_aspects_with_sentiments.to_csv(data_file)

    # Function for detecting the dominant language
    def detect_dominant_language(self, text):
        response = self.comprehend.detect_dominant_language(Text=text)
        return response

    # Function for detecting named entities
    def detect_entities(self, text, language_code):
        response = self.comprehend.detect_entities(Text=text, LanguageCode=language_code)
        return response

    # Function for detecting key phrases
    def detect_key_phraes(self, text, language_code):
        response = self.comprehend.detect_key_phrases(Text=text, LanguageCode=language_code)
        return response

    # Function for detecting sentiment
    def detect_sentiment(self, text, language_code):
        response = self.comprehend.detect_sentiment(Text=text, LanguageCode=language_code)
        return response
