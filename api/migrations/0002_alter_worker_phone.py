# Generated by Django 4.0.2 on 2022-05-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
