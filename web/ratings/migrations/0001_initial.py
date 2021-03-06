# Generated by Django 2.1.7 on 2019-06-04 03:23

from django.db import migrations, models
import djongo.models.fields
import ratings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
                ('reviews', djongo.models.fields.ArrayModelField(model_container=ratings.models.Reviews)),
                ('category', models.CharField(default='NONE', max_length=20)),
                ('location', models.CharField(default='NONE', max_length=20)),
                ('address', models.CharField(default='NONE', max_length=20)),
                ('star_ratings', models.CharField(default='NONE', max_length=5)),
                ('positive_reviews', models.IntegerField(default=0)),
                ('negative_reviews', models.IntegerField(default=0)),
                ('total_reviews', models.IntegerField()),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=5)),
                ('breakfast_food_drink', models.IntegerField(default=0)),
                ('comfort_facilities', models.IntegerField(default=0)),
                ('location_aspects', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('overall', models.IntegerField(default=0)),
                ('service_staff', models.IntegerField(default=0)),
                ('value_for_money', models.IntegerField(default=0)),
            ],
        ),
    ]
