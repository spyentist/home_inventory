from django.db import models
# from django.db.models.fields import CharField

# Create your models here.

class season(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return(self.name)


class item(models.Model):
    name = models.CharField(max_length=40)

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
    items = models.ManyToManyField(item, through='item_container')
    
    def __str__(self):
        return f"{self.location}-{self.row_letter}-{self.column_number}"


class item_container(models.Model):
    quantity = models.IntegerField(default=1)    
    item = models.ForeignKey('item', on_delete=models.CASCADE)
    container = models.ForeignKey('container', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} {self.item} in {self.container}"

    class Meta:
        unique_together = [['item', 'container']]
        verbose_name = 'Items in Container'


