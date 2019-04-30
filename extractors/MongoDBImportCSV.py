import pymongo
import json
from Preprocessor import Preprocessor


class MongoDBImportCSV:
    mongo_client = pymongo.MongoClient('localhost', 27017)

    def __init__(self, file_path, db, collection):
        self.import_content(file_path, db, collection)

    def connect(self, db, collection):
        mongo_db = self.mongo_client[db]
        return mongo_db[collection]

    def get_data(self, file_path):
        preprocessor = Preprocessor()
        return preprocessor.get_data(file_path)

    def csv_to_json(self, file_path):
        data = self.get_data(file_path)
        return json.loads(data.to_json(orient='records'))

    def import_content(self, file_path, db, collection):
        data = self.csv_to_json(file_path)
        collection = self.connect(db, collection)
        collection.remove()
        collection.insert(data)
