# Generated by Django 3.2.4 on 2021-07-22 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210723_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aidefencearticle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ainondefencearticle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.RemoveField(
            model_name='defencearticle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='nondefencearticle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='unclassiedarticle',
            name='date',
        ),
    ]
