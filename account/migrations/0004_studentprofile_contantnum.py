# Generated by Django 3.0.7 on 2021-06-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210615_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='contantnum',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]