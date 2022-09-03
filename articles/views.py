from django.shortcuts import render
from django_filters.rest_framework import \
    DjangoFilterBackend
from rest_framework import \
    viewsets
from rest_framework.viewsets import \
    ModelViewSet
from articles.models import \
    Article, \
    Comment
from articles.permisions import \
    IsOwnerOrStaffOrReadOnly
from articles.serializer import \
    ArticleSerializer, \
    CommentSerializer
from articles.services import get_some_last_comments
from sadmin.models import Link
from libgravatar import Gravatar


def index_page(request):
    comments = get_some_last_comments(2)

    last_article = Article.objects.latest('id')

    data = {
        'articles': Article.objects.all()[1:4],
        'links': Link.objects.all(),
        'comments': comments,
        'last_article': last_article,
        'CommentCount': Comment.objects.filter(article_id=last_article.id).count()
    }

    return render(request, 'index.html', data)


def article_detail(request, art_id):
    comments = get_some_last_comments(4)

    data = {
        'art': Article.objects.get(id=art_id),
        'links': Link.objects.all(),
        'comments': comments
    }
    return render(request, 'article.html', data)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['article_id']
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user
        serializer.save()
