from django.db import models

class movies(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    music = models.CharField(max_length=50)
    year = models.IntegerField()
    def __str__(self):
        return f"{self.name} was released in {self.year}"

