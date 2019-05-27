from classify import Classifier


class Test:
    def __init__(self, y, test_data, classifier, features, x_train, y_train, x_test, results_file):
        self.test(y, test_data, classifier, features, x_train, y_train, x_test, results_file)

    def test(self, y,  test_data, classifier, features, x_train, y_train, x_test, results_file):
        y_test = Classifier().fit_test_classifier(classifier, features, x_train, y_train, x_test)

        self.save_results(y, test_data, y_test, results_file)

    def save_results(self, y, test_data, y_test, results_file):
        results = test_data.copy()
        results[y] = y_test
        print(results.shape)
        results.to_csv(results_file)
