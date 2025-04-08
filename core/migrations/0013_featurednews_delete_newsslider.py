# Generated by Django 5.1.7 on 2025-03-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_newsslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='featured_news/')),
                ('category', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='newsSlider',
        ),
    ]
