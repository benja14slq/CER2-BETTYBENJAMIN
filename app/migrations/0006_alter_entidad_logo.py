# Generated by Django 4.2.6 on 2023-10-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
