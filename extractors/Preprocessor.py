import pandas as pd
from nltk.corpus import stopwords
from nltk import LancasterStemmer, WordNetLemmatizer
import nltk
import string


class Preprocessor:
    # nltk.download('wordnet')
    # nltk.download('punkt')
    # nltk.download('stopwords')

    # Clean, remove stopwords and punctuation
    def text_process(self, text):
        # Check characters to see if they are in punctuation
        no_punctuation = [char for char in text if char not in string.punctuation]

        # Join the characters again to form the string.
        no_punctuation = ''.join(no_punctuation)

        # Now just remove any stopwords
        return [word for word in no_punctuation.split() if word.lower() not in stopwords.words('english')]

    @staticmethod
    def get_data(data_file, sample=500):
        data = pd.read_csv(data_file)
        # print("Total data): {}".format(data))
        # data_random_subset = data.sample(n=sample)
        return data.dropna()

    def get_train_data(self, train_data_file):
        train_data = self.get_data(train_data_file, sample=200000)
        total_train_data = len(train_data)
        print("Total train data: {}".format(total_train_data))
        return train_data

    def get_test_data(self, test_data_file):
        test_data = self.get_data(test_data_file, sample=10000)
        total_test_data = len(test_data)
        print("Total test data): {}".format(total_test_data))
        return test_data

    def convert_rating(self, data, x, y):
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
