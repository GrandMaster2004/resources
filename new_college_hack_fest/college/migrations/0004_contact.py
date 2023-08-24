# Generated by Django 3.2.13 on 2023-01-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_comment_subcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('college_address', models.CharField(max_length=100)),
                ('hostel', models.CharField(max_length=50)),
                ('room_number', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]