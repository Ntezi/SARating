from sklearn.pipeline import Pipeline


class Classifier:

    def fit_train_classifier(self, classifiers, features, x_train, y_train, x_test):
        for classifier in classifiers:
            return self.get_y_test(classifier, features, x_train, y_train, x_test)

    def fit_test_classifier(self, classifier, features, x_train, y_train, x_test):
        return self.get_y_test(classifier, features, x_train, y_train, x_test)

    def get_y_test(self, classifier, features, x_train, y_train, x_test):
        pipeline = Pipeline([
            features,
            ('classifier', classifier),
        ])
        pipeline.fit(x_train, y_train)
        return pipeline.predict(x_test)