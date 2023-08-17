from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=False)
    no_of_members = models.IntegerField(default=1,null=True)
    creator = models.TextField()
    tempOf: models.TextField()