# Generated by Django 4.2.6 on 2023-10-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_alter_item_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='url',
        ),
    ]