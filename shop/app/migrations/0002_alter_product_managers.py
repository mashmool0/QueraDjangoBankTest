# Generated by Django 4.0.4 on 2024-10-02 13:06

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('available', django.db.models.manager.Manager()),
            ],
        ),
    ]
