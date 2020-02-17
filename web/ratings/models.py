from djongo import models


# Create your models here.
class Reviews(models.Model):
    _id = models.ObjectIdField()
    date = models.CharField(max_length=50)
    review = models.TextField()
    stay_date = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    stars = models.SmallIntegerField()
    breakfast_food_drink = models.IntegerField(default=0)
    comfort_facilities = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    overall = models.IntegerField(default=0)
    service_staff = models.IntegerField(default=0)
    value_for_money = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Business(models.Model):
    # _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    # reviews = models.ArrayModelField(
    #     model_container=Reviews,
    # )
    category = models.CharField(max_length=20, default='NONE')
    location = models.CharField(max_length=20, default='NONE')
    # address = models.CharField(max_length=20, default='NONE')
    star_ratings = models.CharField(max_length=5, default='NONE')
    positive_reviews = models.IntegerField(default=0)
    negative_reviews = models.IntegerField(default=0)
    total_reviews = models.IntegerField()
    ratings = models.DecimalField(max_digits=5, decimal_places=2)
    breakfast_food_drink = models.IntegerField(default=0)
    comfort_facilities = models.IntegerField(default=0)
    location_aspects = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    overall = models.IntegerField(default=0)
    service_staff = models.IntegerField(default=0)
    value_for_money = models.IntegerField(default=0)
