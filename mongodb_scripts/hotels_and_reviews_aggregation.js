db.ratings_hotel.aggregate([
    {
        $lookup:
            {
                from: "ratings_review",
                localField: "url",
                foreignField: "company_url",
                as: "reviews"
            }
    },
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
                    },
                "positive_reviews":
                    {
                        $reduce:
                            {
                                input: "$reviews",
                                initialValue: 0,
                                in: {
                                    $add: ["$$value", {$cond: [{$eq: ["$$this.stars", 1]}, 1, 0]}]
                                }
                            }
                    },
                "negative_reviews":
                    {
                        $reduce:
                            {
                                input: "$reviews",
                                initialValue: 0,
                                in: {
                                    $add: ["$$value", {$cond: [{$eq: ["$$this.stars", 0]}, 1, 0]}]
                                }
                            }
                    },
                "total_reviews": {$size: '$reviews'},
            }
    },
    {$out: "ratings_business"}
]);
db.ratings_business.remove( {reviews: {$exists: true, $size: 0}})