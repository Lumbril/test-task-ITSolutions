# Generated by Django 5.0.6 on 2024-06-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='id_announcement',
            field=models.IntegerField(unique=True, verbose_name='id объявления'),
        ),
    ]
