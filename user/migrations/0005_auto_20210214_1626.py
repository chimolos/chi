# Generated by Django 3.1.6 on 2021-02-14 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210214_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': True, 'verbose_name': 'UserProfile', 'verbose_name_plural': 'UserProfiles'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofile',
        ),
    ]
