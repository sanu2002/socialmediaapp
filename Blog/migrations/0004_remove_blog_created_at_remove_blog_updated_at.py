# Generated by Django 4.1.7 on 2023-03-02 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_remove_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
    ]