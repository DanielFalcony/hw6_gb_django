# Generated by Django 4.2.4 on 2023-09-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('hw2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='date_item_add',
            field=models.DateField(),
        ),
    ]
