db.ratings_business.aggregate([
    {
        $project:
            {
                "_id": 0,
                "name": 1,
                "url": 1,
                "category": 1,
                "location":1,
                "address":1,
                "star_ratings":1,
                "reviews":
                    {
                        "_id": 1,
                        "title": 1,
                        "date": 1,
                        "stay_date": 1,
                        "user": 1,
                        "stars": 1,
                        "review": 1,
                        "breakfast_food_drink": 1,
                        "comfort_facilities": 1,
                        "location": 1,
                        "miscellaneous": 1,
                        "overall": 1,
                        "service_staff": 1,
                        "value_for_money": 1,
                    },
                "positive_reviews": 1,
                "negative_reviews": 1,
                "total_reviews": 1,
                "ratings": {
                    $divide: [
                        {
                            $subtract: [
                                {
                                    $divide: [
                                        {$add: ["$positive_reviews", 1.9208]},
                                        {$add: ["$positive_reviews", "$negative_reviews"]}
                                    ],
                                },
                                {
                                    $multiply: [
                                        1.96,
                                        {
                                            $divide: [
                                                {
                                                    $sqrt: {
                                                        $add: [
                                                            {
                                                                $divide: [
                                                                    {
                                                                        $multiply: ["$positive_reviews", "$negative_reviews"]
                                                                    },
                                                                    {
                                                                        $add: ["$positive_reviews", "$negative_reviews"]
                                                                    }
                                                                ]
                                                            },
                                                            0.9604
                                                        ]
                                                    }
                                                },
                                                {
                                                    $add: ["$positive_reviews", "$negative_reviews"]
                                                }
                                            ]
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            $add: [
                                {
                                    $divide: [3.8416, {$add: ["$positive_reviews", "$negative_reviews"]}]
                                },
                                1
                            ]
                        }
                    ]
                },
            }
    },
    {$out: "ratings_business"}
])