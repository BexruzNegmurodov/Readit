# Generated by Django 4.2.1 on 2023-06-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=221)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=221)),
                ('message', models.TextField()),
            ],
        ),
    ]
