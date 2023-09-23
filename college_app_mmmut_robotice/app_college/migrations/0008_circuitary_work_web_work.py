# Generated by Django 3.2.18 on 2023-05-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_college', '0007_team_info_std_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuitary_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image_web', models.ImageField(upload_to='Circuitary_img')),
            ],
        ),
        migrations.CreateModel(
            name='Web_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('image_web', models.ImageField(upload_to='web_img')),
            ],
        ),
    ]
