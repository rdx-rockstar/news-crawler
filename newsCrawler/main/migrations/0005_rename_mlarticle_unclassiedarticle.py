# Generated by Django 3.2.4 on 2021-07-22 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_aidefencearticle_ainondefencearticle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mlArticle',
            new_name='unclassiedArticle',
        ),
    ]
