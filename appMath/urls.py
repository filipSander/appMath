from django.contrib import admin
from django.urls import \
    path, \
    include
from rest_framework.routers import \
    SimpleRouter

from articles.views import \
    article_page, \
    ArticleViewSet

router = SimpleRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', article_page),
]

urlpatterns += router.urls
