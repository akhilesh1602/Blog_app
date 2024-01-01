from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Article(models.Model):
    title = models.TextField(max_length = 256)
    description = models.TextField(max_length = 256)
    created_date = models.DateTimeField(default=datetime.now(), blank=True)
    author = models.ForeignKey(User, default=None , on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    description = models.TextField(max_length = 256)
    comment_by = models.ForeignKey(User, default=None , on_delete = models.CASCADE)
    def __str__(self):
        return self.comment_by
