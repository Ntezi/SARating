import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV, cross_val_score, cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix, make_scorer, recall_score, precision_recall_curve

import pickle


class Train:
    def __init__(self, x, y, classifier, pipeline, classes, model_file):

        self.train(x, y, classifier, pipeline, classes, model_file)

    def train(self, x, y, classifier, pipeline, classes, model_file):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
        print(len(x_train), len(x_test), len(y_train) + len(y_test))

        train_model = pipeline.fit(x_train, y_train)
        predictions = train_model.predict(x_test)

        print('------------------------Accuracy Score------------------------')
        print(train_model.score(x_test, y_test))

        print('------------------------Confusion Matrix------------------------')
        print(classifier)
        print('--classification_report--')
        report = classification_report(y_test, predictions)
        print(report)
        print('--confusion_matrix--')
        report_ = confusion_matrix(y_test, predictions)
        print(report_)

        self.precision_recall(y_test, predictions)

        print('-------------------------End Confusion Matrix-------------------------')

        # print('------------------------Cross Validation------------------------')

        # scoring = {'prec_macro': 'precision_macro', 'rec_macro': make_scorer(recall_score, average='macro')}
        # scores = cross_val_score(train_model, x_test, y_test, cv=5)
        # print(scores)

        # pred = cross_val_predict(train_model, x_test, y_test, cv=5)
        # plt.scatter(y_test, pred)
        # print('-------------------------End Cross Validation-------------------------')
        # Train model on full dataset and save model
        model = pipeline.fit(x, y)

        # save the model to disk
        pickle.dump(model, open(model_file, 'wb'))

        self.plot(y_test, predictions, classes)

    def plot(self, y_test, predictions, classes):

        # Compute confusion matrix
        cnf_matrix = confusion_matrix(y_test, predictions)
        np.set_printoptions(precision=2)

        # Plot non-normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(cnf_matrix, classes=classes,
                                   title='Confusion matrix, without normalization')

        # Plot normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(cnf_matrix, classes=classes, normalize=True,
                                   title='Normalized confusion matrix')

        plt.show()

    def plot_confusion_matrix(self, cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.tight_layout()

    def plot_cross_validation(self):
        pass

    def precision_recall(self, y_test, predictions):
        precision, recall, thresholds = precision_recall_curve(y_test, predictions)
        # create plot
        plt.plot(precision, recall, label='Precision-recall curve')
        plt.xlabel('Precision')
        plt.ylabel('Recall')
        plt.title('Precision-recall curve')
        plt.legend(loc="lower left")