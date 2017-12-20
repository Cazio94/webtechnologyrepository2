from django.db import models

# Create your models here.

class Movie(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    release_date = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    director = models.CharField(max_length=25)
    trailer = models.URLField()
    poster = models.URLField()
    main_image = models.URLField()
    prime_time = models.CharField(max_length=5)
    late_show = models.CharField(max_length=5)
    room = models.CharField(max_length=2)
    onScreen = models.BooleanField(default=False)


def publish(self):
    return self.save()

def __str__(self):
    return self.title
