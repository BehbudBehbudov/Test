# Generated by Django 5.1.7 on 2025-03-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_popularnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularnews',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='featurednews',
            name='content',
            field=models.TextField(default='Default content'),
        ),
        migrations.AlterField(
            model_name='popularnews',
            name='category',
            field=models.CharField(choices=[('biznes', 'Biznes'), ('idman', 'Idman'), ('texnologiya', 'Texnologiya'), ('əyləncə', 'Əyləncə'), ('həyat tərzi', 'Həyat tərzi'), ('qida', 'Qida'), ('elmlər', 'Elmlər'), ('təhsil', 'Təhsil'), ('sağlamlıq', 'Sağlamlıq'), ('korporativ', 'Korporativ'), ('siyasət', 'Siyasət'), ('din', 'Din')], max_length=20),
        ),
    ]
