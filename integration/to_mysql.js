db.ratings_business.aggregate([
    {
        $project:
            {
                "_id": 0,
                "name": 1,
                "url": 1,
                "category": 1,
                "location": 1,
                "star_ratings": 1,
                "positive_reviews": 1,
                "negative_reviews": 1,
                "total_reviews": 1,
                "ratings": 1,
                 "breakfast_food_drink" : 1,
                 "comfort_facilities" : 1,
                 "location_aspects" : 1,
                 "miscellaneous" : 1,
                 "overall" : 1,
                 "service_staff" : 1,
                 "value_for_money" : 1,
            },

    },
    {$out: "ratings_business"}
]);