from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content