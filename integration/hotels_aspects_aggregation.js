db.ratings_business.aggregate([
    {
        $project:
            {
                "_id": 0,
                "name": 1,
                "url": 1,
                "category": 1,
                "location": 1,
                "address": 1,
                "star_ratings": 1,
                "positive_reviews": 1,
                "negative_reviews": 1,
                "total_reviews": 1,
                "ratings": 1,
                "reviews":
                    {
                        "_id": 1,
                        "title": 1,
                        "date": 1,
                        "stay_date": 1,
                        "user": 1,
                        "stars": 1,
                        "review": 1,
                        "aspects": 1,
                        "breakfast_food_drink": 1,
                        "comfort_facilities": 1,
                        "location": 1,
                        "miscellaneous": 1,
                        "overall": 1,
                        "service_staff": 1,
                        "value_for_money": 1,
                    },
                 "breakfast_food_drink" : { "$sum" : "$reviews.breakfast_food_drink" },
                 "comfort_facilities" : { "$sum" : "$reviews.comfort_facilities" },
                 "location_aspects" : { "$sum" : "$reviews.location" },
                 "miscellaneous" : { "$sum" : "$reviews.miscellaneous" },
                 "overall" : { "$sum" : "$reviews.overall" },
                 "service_staff" : { "$sum" : "$reviews.service_staff" },
                 "value_for_money" : { "$sum" : "$reviews.value_for_money" },
            },

    },
    {$out: "ratings_business"}
]);