# Generated by Django 3.1.7 on 2021-03-28 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
    ]