# Generated by Django 3.1.7 on 2021-02-23 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210218_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='minamount',
            new_name='minnumber',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='number',
        ),
    ]