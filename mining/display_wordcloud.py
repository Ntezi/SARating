import os
from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from preprocess import Preprocess, GetFile

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
rwanda = np.array(Image.open(path.join(d, "/Users/ntezi/Pictures/rwanda.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")


def show_wordcloud(data):
    wordcloud = WordCloud(background_color="white", max_words=2000, max_font_size=60, width=768, height=512,
                          stopwords=stopwords, contour_width=3, contour_color='steelblue')  # , mask=rwanda

    # generate word cloud
    wordcloud.generate(str(data))

    # store to file
    # wordcloud.to_file(path.join(d, "rwanda.png"))

    # show
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.figure()
    # plt.imshow(rwanda, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


encoding = 'utf-8'
data_file = GetFile().tripadvisor_hotel_reviews_result_file
data = Preprocess().get_ready_data(data_file, encoding)

positive_reviews = data.loc[data['stars'] == 1]
# negative_reviews = data.loc[data['stars'] == 0]
# show_wordcloud(negative_reviews['review'])
show_wordcloud(data['review'])
