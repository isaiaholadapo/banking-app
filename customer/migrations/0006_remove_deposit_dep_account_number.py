# Generated by Django 3.1.6 on 2021-02-14 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210214_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='dep_account_number',
        ),
    ]
