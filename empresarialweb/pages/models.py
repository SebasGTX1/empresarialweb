from django.db import models


class Page(models.Model):
    key = models.SlugField(verbose_name='Key name', max_length=100, unique=True)
    title = models.CharField(verbose_name='Title', max_length=200)
    content = models.TextField(verbose_name='Content')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
