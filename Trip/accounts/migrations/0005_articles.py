# Generated by Django 2.1 on 2019-05-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_delete_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='')),
                ('post_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
