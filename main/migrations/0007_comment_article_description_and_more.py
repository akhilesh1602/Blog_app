# Generated by Django 4.2.3 on 2024-01-02 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_remove_comment_article_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="article_description",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="created_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2024, 1, 2, 18, 22, 23, 711565)
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2024, 1, 2, 18, 22, 23, 711565)
            ),
        ),
    ]