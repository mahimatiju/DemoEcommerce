# Generated by Django 3.2.13 on 2022-07-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
