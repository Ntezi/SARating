import boto3
import json
import pandas as pd

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
data_file = '../data/collections/train_1.csv'
data = pd.read_csv(data_file, encoding="ISO-8859-1")
# data = data.sample(n=10)


# Function for detecting the dominant language
def detect_dominant_language(text):
    response = comprehend.detect_dominant_language(Text=text)
    return response


# Function for detecting named entities
def detect_entities(text, language_code):
    response = comprehend.detect_entities(Text=text, LanguageCode=language_code)
    return response


# Function for detecting key phrases
def detect_key_phraes(text, language_code):
    response = comprehend.detect_key_phrases(Text=text, LanguageCode=language_code)
    return response


# Function for detecting sentiment
def detect_sentiment(text, language_code):
    response = comprehend.detect_sentiment(Text=text, LanguageCode=language_code)
    return response


def main():
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

    data["sentiment"] = '-'
    for index, row in data.iterrows():
        text = str(row['sentences'])
        result = detect_sentiment(text, language_code)
        print(result['Sentiment'])
        row["sentiment"] = result['Sentiment']

    result_file = '../data/results/sentiment_aws.csv'
    data.to_csv(result_file)


if __name__ == '__main__':
    main()
