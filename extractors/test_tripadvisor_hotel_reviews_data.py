from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

from preprocess import Preprocess, GetFile
from load import LoadResults
from test import Test


class TestTripadvisorHotelReviews:
    def __init__(self, train_data_file, test_data_file, results_file):
        encoding = 'utf-8'
        sample = 500
        x, y = 'text', 'stars'

        train_data = Preprocess().get_ready_data(train_data_file, encoding, 'train')
        # train_data = Preprocess().get_sample_data(train_data_file, sample, encoding)
        train_data = Preprocess().convert_yelp_review_rating(train_data, x, y)

        sample = 100
        test_data = Preprocess().get_ready_data(test_data_file, encoding, 'test')
        # test_data = Preprocess().get_sample_data(test_data_file, sample, encoding)

        self.tester(train_data, test_data, results_file)

    def tester(self, train_data, test_data, results_file):
        x_train = train_data['text']
        y_train = train_data['stars']
        x_test = test_data['review']
        y = 'stars'

        classifier = LogisticRegression(solver='lbfgs')
        features = ('bow', CountVectorizer(analyzer=Preprocess().get_text_tokens))

        Test(y, test_data, classifier, features, x_train, y_train, x_test, results_file)


if __name__ == '__main__':
    train_data_file_name = GetFile().yelp_reviews_train_file
    test_data_file_name = GetFile().tripadvisor_hotel_reviews_data_file
    results_file = GetFile().tripadvisor_hotel_reviews_result_file

    TestTripadvisorHotelReviews(train_data_file_name, test_data_file_name, results_file)
    LoadResults()
