from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline

from Preprocessor import Preprocessor


class Classifier:

    def fit_model(self, classifier, x_train, y_train, x_test):
        preprocessor = Preprocessor()
        pipeline = Pipeline([
            ('vect', CountVectorizer(tokenizer=preprocessor.text_process)),
            ('classifier', classifier),
        ])

        pipeline.fit(x_train, y_train)
        y_test = pipeline.predict(x_test)
        return y_test
