# Generated by Django 3.2.9 on 2021-11-20 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='recipe_name',
            new_name='priority',
        ),
    ]
