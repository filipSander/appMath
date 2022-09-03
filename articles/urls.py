from django.urls import \
    path
from rest_framework.routers import \
    SimpleRouter

from articles.views import \
    index_page, \
    ArticleViewSet, \
    CommentViewSet, article_detail

router = SimpleRouter()
router.register(r'article', ArticleViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', index_page),
    path('article_number_<int:art_id>/', article_detail)

]

urlpatterns += router.urls
