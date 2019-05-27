from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

from train import Train
from preprocess import Preprocess, GetFile


class TrainYelpReviews:

    def __init__(self, train_data_file):
        encoding = 'utf-8'
        sample = 500

        # train_data = Preprocess().get_ready_data(train_data_file, encoding, 'train')
        train_data = Preprocess().get_sample_data(train_data_file, sample, encoding)

        x, y = 'text', 'stars'
        data = Preprocess().convert_yelp_review_rating(train_data, x, y)
        self.trainer(data, x, y)

    def trainer(self, data, x, y):

        classifiers = []
        classifiers.append(LogisticRegression(solver='lbfgs'))  # multi_class='ovr'
        # clfs.append(SVC(probability=True, kernel="linear", class_weight="balanced"))
        # clfs.append(MultinomialNB())
        # clfs.append(SGDClassifier())

        features = ('vect', CountVectorizer(tokenizer=Preprocess().get_text_tokens))
        classes = ['Positive', 'Negative']
        Train(data, x, y, classifiers, features, classes)


if __name__ == '__main__':
    TrainYelpReviews(GetFile().yelp_reviews_train_file)
