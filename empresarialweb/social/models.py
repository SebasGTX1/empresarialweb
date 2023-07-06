from django.db import models


class Link(models.Model):
    key = models.SlugField(verbose_name='Key name', max_length=100, unique=True)
    name = models.CharField(verbose_name='Social red', max_length=200)
    url = models.URLField(verbose_name='Link', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name
