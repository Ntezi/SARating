# from django.db import models
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

    class Meta:
        abstract = True


class Business(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    reviews = models.ArrayModelField(
        model_container=Reviews,
    )
    category = models.CharField(max_length=20)
    positive_reviews = models.IntegerField()
    negative_reviews = models.IntegerField()
    total_reviews = models.IntegerField()
    ratings = models.DecimalField(max_digits=5, decimal_places=2)

    # def __str__(self):
    #     #     return self.url