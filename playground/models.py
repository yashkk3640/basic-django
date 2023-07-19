from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.TextField()
    description = models.TextField()
    creator = models.TextField()
    tempOf: models.TextField()