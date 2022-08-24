from django.contrib import admin
from django.contrib.admin import \
    ModelAdmin
from django.contrib.gis import \
    forms

from .models import \
    Article, \
    Category, \
    Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    forms = PostAdminForm

admin.site.register(Category)
admin.site.register(Comment)
