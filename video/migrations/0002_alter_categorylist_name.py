# Generated by Django 3.2.1 on 2021-06-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylist',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
