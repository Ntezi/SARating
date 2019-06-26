import pandas as pd

categories_ = {
    "Bed & Breakfast",
    "Campgrounds",
    "Car Rental",
    "Guest Houses",
    "Hostels",
    "Hotels",
    "Rest Stops",
    "RV Parks",
    "RV Rental",
    "Resorts",
    "Luggage Storage",
    "Vacation Rentals"
}

yelp_business = pd.read_csv("../data/collections/yelp/business.csv")
yelp_business = yelp_business.dropna()

yelp_review = pd.read_csv("../data/collections/yelp/review.csv")
yelp_review = yelp_review.dropna()

print(yelp_review.head(5))
print(yelp_review.columns.values)

total_reviews = len(yelp_review)
total_business = len(yelp_business)
print("Total reviews: {}".format(total_reviews))
print("Total business): {}".format(total_business))

yelp_review["date"] = pd.to_datetime(yelp_review["date"], format='%Y-%m-%d')
yelp_review['year'] = yelp_review.date.dt.year

business_ids = yelp_business.business_id.values

hotels_categories = categories_

# print("Hotels Categories): {}".format(hotels_categories))

cat_data = yelp_business.loc[yelp_business['business_id'].isin(business_ids)]

# cat_data.categories
categories = []
for cat in cat_data.categories.values:
    all_categories = cat.split(",")
    for x in all_categories:
        if x in hotels_categories:
            categories.append(cat)
#             # try:
#             #     categories[x] = categories[x] + 1
#             # except:
#             #     categories[x] = 1

print(categories)
hotels_travel_businesses = yelp_business.loc[yelp_business['categories'].isin(categories)]

hotels_travel_reviews = yelp_review.loc[yelp_review['business_id'].isin(hotels_travel_businesses.business_id.values)]

total_hotels_travel_reviews = len(hotels_travel_reviews)
print("Total hotels & travel reviews: {}".format(total_hotels_travel_reviews))

file_name = 'yelp_hotel_travel_reviews.csv'
hotels_travel_reviews.to_csv(file_name)
# with open(file_name, 'a') as f:
#     hotels_travel_reviews.to_csv(f, header=False)
