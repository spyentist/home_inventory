from functools import partial
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class season(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return(self.name)


class item(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return(self.name)

class container(models.Model):
    is_partial_choices = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    location = models.CharField(max_length=40)
    row_letter = models.CharField(max_length=1)
    column_number = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)
    season = models.ManyToManyField(season, blank=True)
    is_partial = models.CharField(max_length=1,choices=is_partial_choices, blank=True, default='N')
    items = models.ManyToManyField(item)
    def __str__(self):
        return f"{self.location}-{self.row_letter}-{self.column_number}"



