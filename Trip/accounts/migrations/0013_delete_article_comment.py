# Generated by Django 2.1 on 2019-05-29 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_article_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article_Comment',
        ),
    ]
