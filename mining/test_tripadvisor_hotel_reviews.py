from preprocess import Preprocess, GetFile
from test import Test, ModelFiles
from load import LoadResults
from test import Test


class TestTripadvisorHotelReviews:
    def __init__(self, test_data_file):
        encoding = 'utf-8'

        sample = 100
        test_data = Preprocess().get_ready_data(test_data_file, encoding)
        # test_data = Preprocess().get_sample_data(test_data_file, sample, encoding)

        self.tester(test_data)

    def tester(self, test_data):
        x_test = test_data['review']
        y = 'stars'

        model_file = ModelFiles().logistics_model_file
        results_file = GetFile().tripadvisor_hotel_reviews_result_file

        Test(y, test_data, x_test, model_file, results_file)


if __name__ == '__main__':
    test_data_file_name = GetFile().tripadvisor_hotel_reviews_data_file
    TestTripadvisorHotelReviews(test_data_file_name)
    LoadResults()
