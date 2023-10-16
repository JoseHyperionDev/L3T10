from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    formed_in = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name