from MongoDBImportCSV import MongoDBImportCSV


class LoadResults:
    db = 'sa_rating'
    collection = 'ratings_review'
    file_path = '../data/results/tripadvisor_hotel_reviews_data_results.csv'

    def __init__(self):
        MongoDBImportCSV(self.file_path, self.db, self.collection)


class LoadCompanies:
    db = 'sa_rating'
    collection = 'ratings_hotel'
    file_path = '../data/collections/tripadvisor_hotels.csv'

    def __init__(self):
        MongoDBImportCSV(self.file_path, self.db, self.collection)


if __name__ == "__main__":
    # LoadResults()
    LoadCompanies()
