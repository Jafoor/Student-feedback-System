# Generated by Django 3.0.7 on 2021-06-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210618_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewdetails',
            old_name='given',
            new_name='usergiven',
        ),
    ]