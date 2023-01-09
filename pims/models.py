from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class season(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=25,null=True)
    def __str__(self):
        return(self.name)

    def save(self, *args, **kwargs):
        self.name.title()
        self.slug = slugify(self.name)
        super(season, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("season", kwargs={"slug": self.slug})
    


class item(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=25, null=True)

    def __str__(self):
        return(self.name)

    class Meta:
        ordering=['name']

    def save(self, *args, **kwargs):
        self.name.title()
        if not self.slug:
            self.slug = slugify(self.name)
        super(item, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("itemDetail", kwargs={"slug": self.slug})


class container(models.Model):
    is_partial_choices = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    location = models.CharField(max_length=40)
    row_letter = models.CharField(max_length=1)
    column_number = models.IntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    season = models.ManyToManyField(season, blank=True)
    is_partial = models.CharField(max_length=1,choices=is_partial_choices, blank=True, default='N')
    items = models.ManyToManyField(item, through='item_container')
    slug = models.SlugField(max_length=25, null=True)
    
    def __str__(self):
        return f"{self.location}-{self.row_letter}-{self.column_number}"

    def save(self, *args, **kwargs):
        self.location = self.location.title()
        self.row_letter = self.row_letter.upper()
        if not self.slug: 
            self.slug = slugify(self.__str__)
        super(container, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['location']

    def get_absolute_url(self):
        return reverse("contents", kwargs={"slug": self.slug})



class item_container(models.Model):
    quantity = models.IntegerField(default=1)    
    item = models.ForeignKey('item', on_delete=models.CASCADE)
    container = models.ForeignKey('container', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.item} in {self.container}"

    class Meta:
        unique_together = [['item', 'container']]
        verbose_name = 'Items in Container'
        ordering = [ '-id' ]


