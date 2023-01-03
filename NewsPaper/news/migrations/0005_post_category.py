# Generated by Django 4.1.3 on 2022-12-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
    ]