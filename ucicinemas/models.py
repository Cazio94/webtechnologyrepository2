from django.db import models

# Create your models here.

class Movie(models.Model) :
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    release_date = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    director = models.CharField(max_length=25)
    trailer = models.URLField()
    poster = models.URLField()
    main_image = models.URLField()


def publish(self):
    return self.save()

def __str__(self):
    return self.title
