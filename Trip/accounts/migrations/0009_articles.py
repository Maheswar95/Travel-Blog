# Generated by Django 2.1 on 2019-05-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0008_delete_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='image/')),
                ('post_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
