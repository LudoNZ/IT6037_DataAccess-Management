# Generated by Django 4.1.3 on 2022-11-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='articles',
            name='fields',
        ),
        migrations.AlterField(
            model_name='articles',
            name='about',
            field=models.TextField(max_length=1500),
        ),
    ]
