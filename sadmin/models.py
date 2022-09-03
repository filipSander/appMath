from django.db import models


class Link(models.Model):
    value = models.CharField('Текст ссылки', max_length=40)
    url = models.CharField('url ссылки', max_length=40)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'
