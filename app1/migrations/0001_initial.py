# Generated by Django 4.1.7 on 2023-03-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('lattempt', models.IntegerField()),
                ('accno', models.CharField(max_length=255)),
            ],
        ),
    ]
