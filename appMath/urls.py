from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import \
    path, \
    include

urlpatterns = [
                  path('grappelli/', include('grappelli.urls')),  # grappelli URLS
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('', include('articles.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
