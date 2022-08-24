from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms

from .models import \
    Article, \
    Category, \
    Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    form = PostAdminForm

admin.site.register(Category)
admin.site.register(Comment)
