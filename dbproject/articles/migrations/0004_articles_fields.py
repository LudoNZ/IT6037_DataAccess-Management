# Generated by Django 4.1.3 on 2022-11-26 22:23

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articletypes_remove_articles_fields_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='fields',
            field=models.JSONField(blank=True, default=articles.models.jsonfield_default_value),
        ),
    ]