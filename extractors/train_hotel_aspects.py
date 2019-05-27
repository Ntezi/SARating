import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

from train import Train
from preprocess import Preprocess, GetFile


class TrainYelReviews:

    def __init__(self, train_data_file, encoding):

        train_data = Preprocess().get_ready_data(train_data_file, encoding, 'train')
        x, y = 'sentences', 'aspects'
        self.trainer(train_data, x, y)

    def trainer(self, data, x, y):
        classifiers = []

        # classifiers.append(LogisticRegression(solver='lbfgs'))  # multi_class='ovr'
        # classifiers.append(SVC(probability=True, kernel="linear", class_weight="balanced"))
        classifiers.append(MultinomialNB())
        # classifiers.append(SGDClassifier())

        features = ('bow', CountVectorizer(analyzer=Preprocess().get_text_tokens))
        classes = ['breakfast & food & drink', 'comfort & facilities', 'location', 'miscellaneous', 'Negative',
                   'overall', 'service & staff', 'value for money']
        Train(data, x, y, classifiers, features, classes)


if __name__ == '__main__':
    encoding = 'latin-1'
    TrainYelReviews(GetFile().hotel_aspects_train_file, encoding)
