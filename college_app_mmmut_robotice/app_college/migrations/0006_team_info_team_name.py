# Generated by Django 3.2.18 on 2023-05-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_college', '0005_auto_20230512_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_info',
            name='team_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]