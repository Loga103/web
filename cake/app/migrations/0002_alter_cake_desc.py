# Generated by Django 5.0.3 on 2024-04-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='desc',
            field=models.TextField(),
        ),
    ]
