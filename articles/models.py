from django.db import models
from django.utils import timezone

from django.contrib.auth.models import \
    User


class Category(models.Model):
    title = models.CharField('Название категории', max_length=80)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=150)
    description = models.CharField('Описание', max_length=150, default='Описание не заданно')
    text = models.TextField('Текст статьи')
    img = models.ImageField('Картинка', upload_to='uploads/', default='')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now())
    views = models.IntegerField('Кол-во просмотров', default=0)
    category = models.ManyToManyField(Category, 'Категории')

    def was_publisher_recently(self):
        days_passed = str(-(self.pub_date - timezone.now())).split()[0]

        if days_passed.__len__() >= 2:
            return self.pub_date
        return days_passed + 'дня назад'

    def __str__(self):
        return f'id: {self.id} | {self.title}'

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField('Текст комментария', max_length=500)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
