from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.pipeline import Pipeline

from train import Train
from preprocess import Preprocess, GetFile
from test import Test, ModelFiles


class TrainAspectSentiments:

    def __init__(self, train_data_file):
        encoding = 'latin-1'
        train_data = Preprocess().get_ready_data(train_data_file, encoding)

        x, y = train_data['sentences'], train_data['sentiments']

        self.trainer(x, y)

    def trainer(self, x, y):
        classifier = MultinomialNB(alpha=1e-1)

        pipeline = Pipeline([('vect', CountVectorizer(analyzer=Preprocess().get_text_tokens, ngram_range=(1, 1))),
                             ('tfidf', TfidfTransformer(use_idf=False)),
                             ('clf', classifier), ])

        classes = ['POSITIVE', 'NEGATIVE', 'NEUTRAL', 'MIXED']

        model_file = ModelFiles().naive_model_for_aspect_sentiments_file

        Train(x, y, classifier, pipeline, classes, model_file)


if __name__ == '__main__':
    TrainAspectSentiments(GetFile().aspect_sentiments_train_file)
