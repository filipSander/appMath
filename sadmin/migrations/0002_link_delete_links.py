# Generated by Django 4.1 on 2022-08-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40, verbose_name='Текст ссылки')),
                ('url', models.CharField(max_length=40, verbose_name='url ссылки')),
            ],
            options={
                'verbose_name': 'Ссылку',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]
