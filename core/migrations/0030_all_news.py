# Generated by Django 5.1.7 on 2025-04-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_big_slider', models.BooleanField(default=False)),
                ('is_small_slider', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
