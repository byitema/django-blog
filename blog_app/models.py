from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.title
