from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from train import Train
from preprocess import Preprocess, GetFile
from test import Test, ModelFiles

class TrainYelpReviews:

    def __init__(self, train_data_file):
        encoding = 'utf-8'
        sample = 500

        x_label, y_label = 'text', 'stars'

        # train_data = Preprocess().get_ready_data(train_data_file, encoding')
        train_data = Preprocess().get_sample_data(train_data_file, sample, encoding)

        train_data = Preprocess().convert_yelp_review_rating(train_data, x_label, y_label)

        x, y = train_data['text'], train_data['stars']
        self.trainer(x, y)

    def trainer(self, x, y):
        classifier = LogisticRegression(solver='lbfgs')

        pipeline = Pipeline([('vect', CountVectorizer(analyzer=Preprocess().get_text_tokens, ngram_range=(1, 1))),
                             ('tfidf', TfidfTransformer(use_idf=False)),
                             ('clf', classifier), ])

        classes = ['Positive', 'Negative']

        model_file = ModelFiles().logistics_model_file

        Train(x, y, classifier, pipeline, classes, model_file)

if __name__ == '__main__':
    TrainYelpReviews(GetFile().yelp_reviews_train_file)
