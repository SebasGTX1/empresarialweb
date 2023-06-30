from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitle')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(verbose_name='Image', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
