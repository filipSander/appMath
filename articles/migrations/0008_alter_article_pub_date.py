# Generated by Django 4.1 on 2022-08-24 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 9, 40, 2, 674534, tzinfo=datetime.timezone.utc), verbose_name='Дата публикации'),
        ),
    ]