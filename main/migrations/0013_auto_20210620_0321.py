# Generated by Django 3.0.7 on 2021-06-20 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210619_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewdetails',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ReviewSet'),
        ),
    ]