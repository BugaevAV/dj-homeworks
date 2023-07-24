from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    image = models.URLField() 
    release_date = models.DateField() 
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from = 'name') # type: ignore
    