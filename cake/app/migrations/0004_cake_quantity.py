# Generated by Django 5.0.3 on 2024-04-16 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_desc_cake_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='quantity',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
