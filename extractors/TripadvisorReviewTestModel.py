from sklearn.linear_model import LogisticRegression

from Preprocessor import Preprocessor
from Classifier import Classifier
from load import LoadResults


class TripadvisorReviewTestModel:
    def __init__(self, train_data_file, test_data_file):
        preprocessor = Preprocessor()

        x, y = 'text', 'stars'

        train_data = preprocessor.get_train_data(train_data_file)
        train_data = preprocessor.convert_rating(train_data, x, y)

        test_data = preprocessor.get_test_data(test_data_file)

        self.test(train_data, test_data)

    def test(self, train_data, test_data):
        classifier = LogisticRegression(solver='lbfgs')  # multi_class='multinomial'

        x_train = train_data['text']
        y_train = train_data['stars']
        x_test = test_data['review']

        model = Classifier()
        y_test = model.fit_model(classifier, x_train, y_train, x_test)

        self.save_results(test_data, y_test)

    def save_results(self, test_data, y_test):
        result_file = '../data/results/tripadvisor_hotel_reviews_data_results.csv'
        results = test_data.copy()
        results['stars'] = y_test
        print(results.shape)
        results.to_csv(result_file)


if __name__ == '__main__':
    train_data_file_name = "../data/train/yelp_hotel_travel_reviews.csv"
    test_data_file_name = "../data/test/tripadvisor_hotel_reviews_data.csv"
    TripadvisorReviewTestModel(train_data_file_name, test_data_file_name)
    LoadResults()
