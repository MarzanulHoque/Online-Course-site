# Generated by Django 3.1.2 on 2021-02-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210201_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='Title', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
