# Generated by Django 4.0.4 on 2024-05-05 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='comments',
        ),
    ]