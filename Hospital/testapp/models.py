from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.IntegerField()
