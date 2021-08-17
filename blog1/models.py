from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=225)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author=models.CharField(max_length=13)
    likes=models.ManyToManyField(User, related_name='likes', blank=True)
    timestamp=models.DateTimeField(blank=True)
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+'by' + ' ' + self.author