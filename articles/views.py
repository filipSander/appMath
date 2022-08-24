from django.shortcuts import render
from django_filters.rest_framework import \
    DjangoFilterBackend
from rest_framework.viewsets import \
    ModelViewSet

from articles.models import \
    Article
from articles.serializer import \
    ArticleSerializer


def article_page(request):
    return render(request, 'index.html', {'articles': Article.objects.all()})


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']

