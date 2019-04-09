#!/usr/bin/env python
import os
import sys
import pandas as pd
import pymongo
import json


def import_content(file_path):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['test']  # Replace mongo db name
    collection_name = 'hotels'  # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, file_path)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)


if __name__ == "__main__":
    file_path = '../data/results/tripadvisor_hotel_reviews_data_results.csv'  # pass csv file path
    import_content(file_path)
