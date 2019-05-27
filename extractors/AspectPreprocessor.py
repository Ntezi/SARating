from __future__ import unicode_literals, print_function
from spacy.lang.en import English  # updated
from Preprocessor import Preprocessor
import pandas as pd
import nltk

preprocessor = Preprocessor()
data_file = '../data/results/tripadvisor_hotel_reviews_data_results.csv'
data = preprocessor.get_sample_data(data_file, 5)

positive_reviews = data.loc[data['stars'] == 1]
negative_reviews = data.loc[data['stars'] == 0]
# text = positive_reviews['review']
# text = "Super friendly staff, helpful in organizing Transportation, etc. , free Airport shuttle pickup, clean room, hot water, nice Food in the Restaurant, good choices for breakfastm excellent coffee, nice garden and Terrasse with view over Kigali. safe place with security. strong wifi. Thank you so much for everything which made our stay outstanding. We would definitely come back when in Kigali."

nlp = English()
nlp.add_pipe(nlp.create_pipe('sentencizer'))

sentences = []

for index, row in data.iterrows():
    doc = nlp(str(row['review']))
    for sent in doc.sents:
        sentences.append(sent.text)
    # sentences = [sent.string.strip() for sent in doc.sents]

df_sentences = pd.DataFrame()
df_sentences['sentences'] = sentences

stopwords = nltk.corpus.stopwords.words('english')


for _, row in df_sentences.iterrows():
    tokens = nltk.tokenize.word_tokenize(str(row['sentences']))
    tokens = [token for token in tokens if not token in stopwords]

    # for token in tokens:
    #      df_sentences['tokens'] = token
    # print(tokens)
    #
    # df_tokens = pd.DataFrame()
    # df_tokens['tokens'] = tokens
    #
    # print(df_tokens.shape)

result_file = '../data/results/sentences.csv'
df_sentences.to_csv(result_file)

# print(sentences)
