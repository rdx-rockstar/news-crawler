# Generated by Django 3.2.4 on 2021-07-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210723_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aidefencearticle',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ainondefencearticle',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='defencearticle',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nondefencearticle',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unclassiedarticle',
            name='date',
            field=models.CharField(max_length=255),
        ),
    ]
