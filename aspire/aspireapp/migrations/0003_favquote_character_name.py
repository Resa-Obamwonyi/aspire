# Generated by Django 3.1.2 on 2021-04-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspireapp', '0002_auto_20210422_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='favquote',
            name='character_name',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]