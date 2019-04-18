# Generated by Django 2.1.7 on 2019-04-18 08:25

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
                ('category', models.CharField(max_length=20)),
                ('positive_reviews', models.IntegerField()),
                ('negative_reviews', models.IntegerField()),
                ('total_reviews', models.IntegerField()),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
