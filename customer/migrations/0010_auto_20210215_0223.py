# Generated by Django 3.1.6 on 2021-02-15 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_withdraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='with_username',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
