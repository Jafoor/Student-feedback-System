# Generated by Django 3.0.7 on 2021-06-18 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_studentprofile_year_semester'),
        ('main', '0003_auto_20210618_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dept'),
        ),
    ]