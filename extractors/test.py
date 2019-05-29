import pickle


class Test:

    def __init__(self, y, test_data, x_test, model_file, results_file):
        self.test(y, test_data, x_test, model_file, results_file)

    def test(self, y, test_data, x_test, model_file, results_file):
        model = pickle.load(open(model_file, 'rb'))

        y_test = model.predict(x_test)

        self.save_results(y, test_data, y_test, results_file)

    def save_results(self, y, test_data, y_test, results_file):
        results = test_data.copy()
        results[y] = y_test
        print(results.shape)
        results.to_csv(results_file)


class ModelFiles:
    naive_model_file = '../data/python/naive_model.pkl'
    logistics_model_file = '../data/python/logistics_model_file.pkl'
