# Generated by Django 4.2.7 on 2023-12-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallchop', '0004_rename_quantity_eventitem_guest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventitem',
            old_name='evtproduct',
            new_name='chops',
        ),
    ]