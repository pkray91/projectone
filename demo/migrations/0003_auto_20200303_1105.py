# Generated by Django 3.0 on 2020-03-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
