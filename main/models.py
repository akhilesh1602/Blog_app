from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.TextField(max_length = 256)
    description = models.TextField(max_length = 256)
    created_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
