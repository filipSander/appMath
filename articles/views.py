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
from sadmin.models import \
    Link


def article_page(request):

    data = {
        'articles': Article.objects.all()[:4],
        'links': Link.objects.all(),
        'Comments': Comment.objects.all()[:2]

    }
    return render(request, 'index.html', data)


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
