import pymongo
import json
from preprocess import Preprocess, GetFile


class MongoDBImportCSV:
    mongo_client = pymongo.MongoClient('localhost', 27017)
    encoding = 'utf-8'

    def __init__(self, file_path, db, collection):
        self.import_content(file_path, db, collection)

    def connect(self, db, collection):
        mongo_db = self.mongo_client[db]
        return mongo_db[collection]

    def get_data(self, file_path):
        return Preprocess().get_data(file_path, self.encoding)

    def csv_to_json(self, file_path):
        data = self.get_data(file_path)
        return json.loads(data.to_json(orient='records'))

    def import_content(self, file_path, db, collection):
        data = self.csv_to_json(file_path)
        collection = self.connect(db, collection)
        collection.remove()
        collection.insert(data)


class LoadResults:
    db = 'sa_rating'
    collection = 'ratings_review'
    # file_path = '../data/results/tripadvisor_hotel_reviews_data_results.csv'
    file_path = GetFile().tripadvisor_hotel_reviews_result_file

    def __init__(self):
        MongoDBImportCSV(self.file_path, self.db, self.collection)


class LoadCompanies:
    db = 'sa_rating'
    collection = 'ratings_hotel'
    file_path = '../data/collections/tripadvisor_hotels.csv'

    def __init__(self):
        MongoDBImportCSV(self.file_path, self.db, self.collection)


if __name__ == "__main__":
    LoadResults()
    # LoadCompanies()
