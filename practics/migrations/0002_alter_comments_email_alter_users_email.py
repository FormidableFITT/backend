# Generated by Django 4.2 on 2023-04-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
