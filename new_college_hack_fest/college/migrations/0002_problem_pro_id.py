# Generated by Django 3.2.13 on 2023-01-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='pro_id',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]