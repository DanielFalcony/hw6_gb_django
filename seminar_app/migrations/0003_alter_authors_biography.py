# Generated by Django 4.2.4 on 2023-09-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('seminar_app', '0002_authors_alter_gamemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='biography',
            field=models.TextField(max_length=1000),
        ),
    ]
