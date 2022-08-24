from django.utils import \
    timezone

from django.urls import \
    reverse
from rest_framework import \
    status
from rest_framework.test import APITestCase

from articles.models import \
    Article
from articles.serializer import \
    ArticleSerializer


class ArticlesApiTestCase(APITestCase):
    def test_get(self):
        article_1 = Article.objects.create(title='Статья 1', text='some text', pub_date=timezone.now(), views=0)
        article_2 = Article.objects.create(title='Статья 2T', text='some text', pub_date=timezone.now(), views=0)

        url = reverse('article-list')
        print(url)
        responsive = self.client.get(url)
        print(responsive.data)
        serializer_data = ArticleSerializer([article_1, article_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, responsive.status_code)
        self.assertEqual(serializer_data, responsive.data)