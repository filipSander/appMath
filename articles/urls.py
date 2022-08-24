from django.urls import \
    path
from rest_framework.routers import \
    SimpleRouter

from articles.views import \
    article_page, \
    ArticleViewSet

router = SimpleRouter()
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('', article_page),
]

urlpatterns += router.urls
