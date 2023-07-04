from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    published = models.DateTimeField(verbose_name="Publish Date", default=now)
    image = models.ImageField(verbose_name='Image', upload_to='blog')
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categories', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
