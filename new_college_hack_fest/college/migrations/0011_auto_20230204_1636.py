# Generated by Django 3.2.13 on 2023-02-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_hostel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='troom',
            new_name='total_alloted_room',
        ),
        migrations.AddField(
            model_name='hostel',
            name='total_empty_rooms',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
