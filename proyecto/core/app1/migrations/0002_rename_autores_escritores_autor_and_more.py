# Generated by Django 4.0.1 on 2022-01-17 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escritores',
            old_name='autores',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='escritores',
            old_name='libros',
            new_name='libro',
        ),
    ]
