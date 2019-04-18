db.business.aggregate([
    {
        $project:
            {
                "_id": 0,
                "name": 1,
                "url": 1,
                "category": 1,
                "reviews":
                    {
                        "_id": 1,
                        "title": 1,
                        "date": 1,
                        "stay_date": 1,
                        "user": 1,
                        "stars": 1,
                        "review": 1,
                    },
                "positive_reviews": 1,
                "negative_reviews": 1,
                "total_reviews": 1,
                "ratings": {"$multiply": [{"$divide": ["$positive_reviews", "$total_reviews"]}, 5]}
            }
    },
    {$out: "business"}
])