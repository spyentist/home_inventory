# Generated by Django 3.2.5 on 2021-07-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pims', '0003_auto_20210725_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='random_col',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
