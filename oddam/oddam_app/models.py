from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    TYPES = (
        (1, 'fundacja'),
        (2, 'organizacja pozarządowa'),
        (3, 'zbiórka lokalna')

    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = ManyToManyField(Category)
