# Generated by Django 4.2.1 on 2023-06-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subblog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
    ]
