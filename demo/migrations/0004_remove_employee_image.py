# Generated by Django 3.0 on 2020-03-05 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200303_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
    ]
