from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.year}"


class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)