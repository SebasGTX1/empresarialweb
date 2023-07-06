from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name='Key name', max_length=100, unique=True)
    name = models.CharField(verbose_name='Social red', max_length=200)
    url = 
    created =
    updated =
