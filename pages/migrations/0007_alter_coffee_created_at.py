# Generated by Django 4.2 on 2023-05-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_coffee_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]