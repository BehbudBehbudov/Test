# Generated by Django 5.1.7 on 2025-03-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_trendingnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('category', models.CharField(max_length=50)),
                ('published_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
