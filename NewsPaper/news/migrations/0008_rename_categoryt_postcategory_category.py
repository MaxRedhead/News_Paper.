# Generated by Django 4.1.3 on 2022-12-15 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_rename_category_postcategory_categoryt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='categoryT',
            new_name='category',
        ),
    ]