from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(blank=False)
