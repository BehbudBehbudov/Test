# Generated by Django 5.1.7 on 2025-03-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_small_slider_delete_small_slider_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='newsSlider_news/')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(default='Default content')),
                ('category', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_activate', models.BooleanField(default=True)),
            ],
        ),
    ]
