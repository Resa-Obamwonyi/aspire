# Generated by Django 3.1.2 on 2021-04-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspireapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favquote',
            name='character_id',
            field=models.CharField(max_length=255),
        ),
    ]
