# Generated by Django 4.2.3 on 2024-01-01 08:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0002_article_author_alter_article_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2024, 1, 1, 14, 14, 40, 569767)
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(max_length=256)),
                (
                    "comment_by",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
