# Generated by Django 2.1.5 on 2019-01-23 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]
