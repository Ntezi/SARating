from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

from Preprocessor import Preprocessor
from TrainingResults import TrainingResults
from Classifier import Classifier


class YelpReviewTrainer:
    def __init__(self, train_data_file):
        preprocessor = Preprocessor()
        train_data = preprocessor.get_train_data(train_data_file)
        x, y = 'text', 'stars'

        data = preprocessor.convert_rating(train_data, x, y)
        self.train(data, x, y)

    def train(self, data, x, y):
        x_train, x_test, y_train, y_test = train_test_split(data[x], data[y], test_size=0.2, random_state=42)
        print(len(x_train), len(x_test), len(y_train) + len(y_test))

        clfs = []
        clfs.append(LogisticRegression(solver='lbfgs'))  # multi_class='ovr'
        # clfs.append(SVC(probability=True, kernel="linear", class_weight="balanced"))
        # clfs.append(MultinomialNB())
        # clfs.append(SGDClassifier())
        for classifier in clfs:
            model = Classifier()
            predictions = model.fit_model(classifier, x_train, y_train, x_test)

            print('------------------------Start------------------------')
            print(classifier)
            print('--classification_report--')
            report = classification_report(y_test, predictions)
            print(report)
            print('--confusion_matrix--')
            report_ = confusion_matrix(y_test, predictions)
            print(report_)
            print('-------------------------End-------------------------')

            TrainingResults(y_test, predictions)


if __name__ == '__main__':
    train_data_file_name = "data/train/yelp_hotel_travel_reviews.csv"
    YelpReviewTrainer(train_data_file_name)
