# Generated by Django 3.2.5 on 2021-07-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210722_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
