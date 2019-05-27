import os
from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from Preprocessor import Preprocessor

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
rwanda = np.array(Image.open(path.join(d, "/Users/ntezi/Pictures/rwanda.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")


def show_wordcloud(data):
    wc = WordCloud(background_color="white", max_words=2000, mask=rwanda,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(str(data))

    # store to file
    wc.to_file(path.join(d, "rwanda.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(rwanda, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


preprocessor = Preprocessor()
data_file = '../data/results/tripadvisor_hotel_reviews_data_results.csv'
data = preprocessor.get_sample_data(data_file, 10000)

positive_reviews = data.loc[data['stars'] == 1]
# negative_reviews = data.loc[data['stars'] == 0]
# show_wordcloud(negative_reviews['review'])
show_wordcloud(positive_reviews['review'])
