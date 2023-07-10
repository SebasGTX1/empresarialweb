from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    content = RichTextField(verbose_name='Content')
    order = models.SmallIntegerField(verbose_name='Order', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ['order', 'title']

    def __str__(self) -> str:
        return self.title
