# Generated by Django 4.1 on 2022-08-17 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_category_delete_artcat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
