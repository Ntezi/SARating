import pandas as pd
from nltk.corpus import stopwords
import nltk
import string


class Preprocess:
    # nltk.download('wordnet')
    # nltk.download('punkt')
    # nltk.download('stopwords')

    # Clean, remove stopwords and punctuation
    def get_text_tokens(self, text):
        # Check characters to see if they are in punctuation
        no_punctuation = [char for char in text if char not in string.punctuation]

        # Join the characters again to form the string.
        no_punctuation = ''.join(no_punctuation)

        # Now just remove any stopwords
        return [word for word in no_punctuation.split() if word.lower() not in stopwords.words('english')]

    def get_data(self, data_file, encoding):
        data = pd.read_csv(data_file, encoding=encoding, index_col=0)
        return data.dropna()

    def get_ready_data(self, train_data_file, encoding):
        data = self.get_data(train_data_file, encoding)
        total = len(data)
        print("Total data: {}".format(total))
        return data

    def get_sample_data(self, data_file, sample, encoding):
        data = self.get_data(data_file, encoding)
        data_random_subset = data.sample(n=sample)
        # print("Total sample data: {}".format(data_random_subset))
        return data_random_subset.dropna()

    def convert_yelp_review_rating(self, data, x, y):
        data['length'] = data[x].apply(len)
        data['date'] = pd.to_datetime(data['date'])

        # Convert five classes into two classes (positive = 1 and negative = 0)
        data[y] = data[y].map(lambda a: 1 if int(a) > 3 else 0)

        return data

        # ---------------------------------------------------------

    def stem_words(self, words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self, words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas


class GetFile:
    hotel_aspects_train_file = '../data/collections/train_1.csv'
    yelp_reviews_train_file = '../data/train/yelp_hotel_travel_reviews.csv'
    hotel_aspects_test_file = "../data/results/sentences.csv"
    hotel_aspects_result_file = '../data/results/aspect_data_results.csv'
    tripadvisor_hotel_reviews_data_file = '../data/test/tripadvisor_hotel_reviews_data.csv'
    tripadvisor_hotel_reviews_result_file = '../data/results/tripadvisor_hotel_reviews_data_results.csv'
    tripadvisor_hotel_reviews_result_merged_with_aspects_file = '../data/results/tripadvisor_hotel_reviews_result_merged_with_aspects_file.csv'
    sentences_file = '../data/results/sentences_file.csv'
    aspects_file = '../data/results/aspects_file.csv'
    sentences_with_aspects_file = '../data/results/sentences_with_aspects_file.csv'
    aspects_with_sentiment_aws_file = '../data/results/aspects_with_sentiment_aws_file.csv'
    aspect_sentiments_train_file = '../data/train/aspect_sentiments_train_file.csv'
