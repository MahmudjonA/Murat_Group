# Generated by Django 5.0.6 on 2024-05-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='media/images')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_img', models.ImageField(null=True, upload_to='media/images')),
                ('aboutCompany', models.CharField(max_length=150)),
                ('history', models.CharField(max_length=150)),
                ('founder', models.CharField(max_length=150)),
                ('founded_year', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
            ],
        ),
    ]
