# Generated by Django 3.2.5 on 2021-07-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_generalconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfig',
            name='key',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
