from django.db import models


class movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} from {self.year}"


class me(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
